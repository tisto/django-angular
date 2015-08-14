(function() {
  'use strict';

  angular.module('myApp', ['angular-loading-bar', 'restangular']);

  angular.module('myApp').controller('TextController',
    function($scope) {
      var someText = {};
      someText.message = 'Hi angular world!';
      $scope.someText = someText;
    }
  );

  angular.module('myApp').controller('UsersController',
    function($scope, Restangular) {
      var baseUsers = Restangular.all('users');

      $scope.newId = 3;
      function generatedUniqueId() {
        $scope.newId += 1;
        return $scope.newId - 1;
      }

      $scope.listUsers = function() {
        baseUsers.getList().then(function(users) {
          $scope.users = users;
        }, function(response) {
          console.log("Error with status code", response.status);
        });
      }

      $scope.createUser = function(userTitle) {
        baseUsers.post({
          'id': generatedUniqueId(),
          'title': userTitle
        });
        $scope.userTitle = '';
        $scope.listUsers();
      }

      $scope.deleteUser = function(user) {
        user.remove().then(function() {
          // edited: a better solution, suggested by Restangular themselves
          // since previously _.without() could leave you with an empty non-restangular array
          // see https://github.com/mgonto/restangular#removing-an-element-from-a-collection-keeping-the-collection-restangularized
          var index = $scope.users.indexOf(user);
          if (index > -1) $scope.users.splice(index, 1);
        }, function(response) {
          console.log("Error with status code", response.status);
        });
      }

      $scope.listUsers();

    }
  );

})();
