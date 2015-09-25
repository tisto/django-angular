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
    function($scope, $timeout, jsonSchemaService) {

      $scope.model = {};
      $scope.schema = {};
      $scope.form = [];

      jsonSchemaService.get_schema().success(function(data, status) {
        $scope.schema = data;
        $scope.form = data.form;

        // Customize Form appearance
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
      });

      $scope.onSubmit = function(form) {
        // First we broadcast an event so all fields validate themselves
        $scope.$broadcast('schemaFormValidate');

        // Then we check if the form is valid
        if (form.$valid) {
          console.log('check if form is valid');
        }
      }

      $scope.clearForm = function(form) {
        $scope.model = {};
        $scope.$broadcast('schemaFormRedraw');
      }

    }
  );

})();
