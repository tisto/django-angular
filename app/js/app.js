(function() {
  'use strict';

  angular.module('myApp', [
    'angular-loading-bar',
    'schemaForm',
    'schemaForm-datepicker',
    'schemaForm-timepicker',
    'schemaForm-datetimepicker'
  ]);

  angular.module('myApp').factory('httpRequestInterceptor', [
    function() {
      return {
        request: function(config) {
          config.headers = {
            'Accept': 'application/schema+json',
            'Access-Control-Allow-Origin': 'localhost:8000'
          };
          return config;
        }
      }
    }
  ]);

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

      $scope.schema = {};

      jsonSchemaService.get_schema().success(function(data, status) {
        $scope.schema = data;
      });

      $scope.form = [
        "*",
        {
          type: "button",
          title: "Cancel",
          style: 'btn-default',
          onClick: "clearForm(form)"
        },
        {
          type: "submit",
          title: "Save"
        }
      ];

      $scope.model = {};

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
