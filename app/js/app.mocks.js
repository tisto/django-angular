(function() {
  'use strict';

  angular.module('e2e-mocks', ['ngMockE2E']).run(function($httpBackend) {

    // --- REST JOB SERVICE --------------------------------------------------

    var users = {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": "0",
                "url": "http://127.0.0.1:8000/users/1/",
                "username": "admin",
                "email": "",
                "groups": []
            }
        ]
    };

    function usersIndexById(id) {
      if (!id) return null;
      var index = -1;

      for(var i = 0; i < users.results.length; i++) {
        var o = users.results[i];
        if (id == o.id) {
          index = i;
          break;
        }
      }

      return index;
    }

    // LIST JOBS
    $httpBackend.when('GET', '/users').respond(
      function(method, url, data, headers) {
        console.log('[MOCK] GET /users');
        return [200, users.results];
      }
    );

    // CREATE JOB
    $httpBackend.when('POST', '/users').respond(
      function(method, url, data, headers) {
        console.log('[MOCK] POST /users ' + data);
        users.results.push(angular.fromJson(data));
        return [201];
      }
    )

    // READ JOB
    /*
    $httpBackend.when('GET', '/api/users/1').respond(
      function(method, url, data, headers) {
        return [200, job[0]];
      }
    );*/

    // UPDATE JOB
    /*
    $httpBackend.when('PUT', '/api/users/1').respond(
      return [200, {status: 'OK'}];
    )
    */

    // DELETE JOB
    var usersRegExp = new RegExp(/\/users\/(\d*)*/);
    $httpBackend.when('DELETE', usersRegExp).respond(
      function(method, url, data, headers) {
        var match = usersRegExp.exec(url);
        var jobId = parseInt(match[1]);
        var index = usersIndexById(jobId);
        console.log('[MOCK] DELETE /users/' + jobId);
        users.results.splice(index, 1);
        return [204, {status: 'No content'}];
      }
    )

    // --- PASS THROUGH TEMPLATES --------------------------------------------
    var templates_re = new RegExp('.*.html$');
    $httpBackend.whenGET(templates_re).passThrough();

  });

  angular.module('myApp').requires.push('e2e-mocks');

})();
