(function() {
  'use strict';

  angular.module('myApp', [
    'angular-loading-bar',
    'mgcrea.ngStrap',
    'schemaForm',
    'schemaForm-datepicker',
    'schemaForm-timepicker',
    'schemaForm-datetimepicker'
  ]);

  angular.module('myApp').run(function($http) {
    // Make Angular send Accept: 'application/schema+json' by default
    $http.defaults.headers.common.Accept = 'application/schema+json'
  });

  angular.module('myApp').factory('jsonSchemaService',
    function($http) {
      var getJsonSchema = function() {
        var url = 'http://localhost:8000/application/';
        return $http({
          method: 'GET',
          url: url
        }).error(function(data, status) {
          alert('Error accessing "' + url + '" Status: ' + status);
        });
      };
      return {
        get_schema: function() {
          return getJsonSchema();
        }
      };
    }
  );

  angular.module('myApp').controller('FormController',
    function($scope, $timeout, $q, jsonSchemaService) {

      $scope.model = {};
      $scope.schema = {};
      $scope.form = [];

      jsonSchemaService.get_schema().success(function(data, status) {
        $scope.schema = data;
        $scope.form = data.form;

        // Customize form fieldsets
        $scope.schema.form.push(
          {
            type: 'fieldset',
            items: [
              'attachment', 'image'
            ]
          }
        );
        var attachmentIndex = $scope.schema.form.indexOf('attachment');
        var imageIndex = $scope.schema.form.indexOf('image');
        $scope.schema.form.splice(attachmentIndex, 1);
        $scope.schema.form.splice(imageIndex, 1);

        // Customize form appearance
        var descriptionIndex = $scope.schema.form.indexOf('description');
        $scope.schema.form[descriptionIndex] = {
          'key': 'description',
          'title': 'Description',
          'description': 'Describe your application.',
          'type': 'textarea',
          'placeholder': 'Description of the application.'
        };
        $scope.schema.form.splice(
          descriptionIndex,
          0,
          {
            type: "template",
            template: '<h4>Detailed <i>HTML</i> <u>description</u> for the {{form.name}} field! <a href="#" ng-click="form.click()">Link</a></h4>',
            name: 'Description',
            click: function() { alert('Link clicked'); }
          }
        );

        var salutationIndex = $scope.schema.form.indexOf('salutation');
        $scope.schema.form[salutationIndex] = {
          'key': 'salutation',
          'placeholder': ' '
        };
        $scope.schema['properties']['salutation'] = {
          'title': "Salutation",
          'type': "string",
          'enum': ["Mr.", "Mrs.", "Ms."],
          'description': "Choose a salutation"
        };

        var usernameIndex = $scope.schema.form.indexOf('username');
        $scope.schema.form[usernameIndex] = {
          key: 'username',
          placeholder: 'Anything but "Bob"',
          $asyncValidators: {
            'async': function(username) {
              var deferred = $q.defer();
              $timeout(function(){
                if (angular.isString(username) && username.toLowerCase().indexOf('bob') !== -1) {
                  deferred.reject();
                } else {
                  deferred.resolve();
                }
              }, 500);
              return deferred.promise;
            }
          },
          validationMessage: {
            'async': "Wooohoo thats not an OK name!"
          }
        };

        var firstnameIndex = $scope.schema.form.indexOf('firstname');
        $scope.schema.form[firstnameIndex] = {
          'type': 'section',
          'htmlClass': 'row',
          'items': [
            {
              'type': 'section',
              'htmlClass': 'col-xs-6',
              'items': [
                'firstname'
              ]
            },
            {
              'type': 'section',
              'htmlClass': 'col-xs-6',
              'items': [
                'lastname'
              ]
            }
          ]
        };
        var lastnameIndex = $scope.schema.form.indexOf('lastname');
        $scope.schema.form[lastnameIndex] = {
          'type': 'section',
          'htmlClass': 'row',
          'items': []
        };
        var streetIndex = $scope.schema.form.indexOf('street');
        $scope.schema.form[streetIndex] = {
          'type': 'section',
          'htmlClass': 'row',
          'items': [
            {
              'type': 'section',
              'htmlClass': 'col-xs-10',
              'items': [
                'street'
              ]
            },
            {
              'type': 'section',
              'htmlClass': 'col-xs-2',
              'items': [
                'house_number'
              ]
            }
          ]
        };
        var houseNumberIndex = $scope.schema.form.indexOf('house_number');
        $scope.schema.form[houseNumberIndex] = {
          'type': 'section',
          'htmlClass': 'row',
          'items': []
        };

        var firstTimeApplicationReasonIndex = $scope.schema.form.indexOf('first_time_application_reason');
        $scope.schema.form[firstTimeApplicationReasonIndex] = {
          "key": "first_time_application_reason",
          "condition": "model.first_time_application"
        };

        Array.prototype.move = function (old_index, new_index) {
          if (new_index >= this.length) {
            var k = new_index - this.length;
            while ((k--) + 1) {
              this.push(undefined);
            }
          }
          this.splice(new_index, 0, this.splice(old_index, 1)[0]);
          return this; // for testing purposes
        };

        var finalizeFormSchema = function() {
          console.log('finalizeFormSchema');
          var form_length = $scope.schema.form.length;
          // move submit, button, actions to the bottom of the form
          for (var fieldIndex in $scope.schema.form) {
            if ($scope.schema.form[fieldIndex]['type'] == 'submit') {
              $scope.schema.form.move(fieldIndex, form_length - 1);
            }
          }
          for (var fieldIndex in $scope.schema.form) {
            if ($scope.schema.form[fieldIndex]['type'] == 'button') {
              $scope.schema.form.move(fieldIndex, form_length - 1);
            }
          }
        }
        finalizeFormSchema();

      });

      $scope.onSubmit = function(form) {
        // First we broadcast an event so all fields validate themselves
        $scope.$broadcast('schemaFormValidate');

        // Then we check if the form is valid
        if (form.$valid) {
          console.log('form is valid');
          $scope.schema.form[0].helpvalue = '<div class="alert alert-success">Form has been successfully submitted.</div>'
        } else {
          $scope.schema.form[0].helpvalue = '<div class="alert alert-danger">Please check your form.</div>'
          console.log('form is invalid');
        }
      }

      $scope.clearForm = function(form) {
        $scope.model = {};
        $scope.$broadcast('schemaFormRedraw');
        // XXX: We expect the help message to be always present as first item
        // in the array. This is fragile.
        $scope.schema.form[0].helpvalue = '<div class="alert alert-info">Form cleared.</div>'
      }

    }
  );

})();
