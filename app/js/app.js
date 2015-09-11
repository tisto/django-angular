(function() {
  'use strict';

  angular.module('myApp', ['angular-loading-bar', 'schemaForm']);

  angular.module('myApp').controller('FormController', function($scope) {
    $scope.schema = {"type": "object", "properties": {"description": {"type": "string", "key": "description", "title": "description"}, "firstname": {"type": "string", "key": "firstname", "title": "firstname"}, "title": {"type": "string", "key": "title", "title": "title"}, "url": {"type": "string", "key": "url", "title": "url"}, "lastname": {"type": "string", "key": "lastname", "title": "lastname"}, "age": {"type": "integer", "key": "age", "title": "age"}, "id": {"type": "integer", "key": "id", "title": "ID"}, "attachment": {"type": "string", "key": "attachment", "title": "attachment"}, "image": {"type": "string", "key": "image", "title": "image"}, "gender": {"type": "string", "key": "gender", "title": "gender"}, "date": {"type": "string", "key": "date", "title": "date"}, "first_time_application": {"type": "boolean", "key": "first_time_application", "title": "first_time_application"}, "email": {"type": "string", "key": "email", "title": "email"}, "uuid": {"type": "string", "key": "uuid", "title": "uuid"}}, "title": "Application(id, title, firstname, lastname, email, age, description, date, attachment, image, url, uuid, gender, first_time_application)"};

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

  });

})();
