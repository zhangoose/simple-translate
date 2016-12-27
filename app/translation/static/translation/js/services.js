angular.module('translationApp.services', ['ngResource'])
    .factory('Translation', function($resource, ENV) {
        var headers = {
            "Content-Type": "application/json",
            "Authorization": ENV.API_TOKEN
        };

        return $resource(
            '/api/translations/',
            {},
            {
                'query': {
                    method: 'GET',
                    isArray: true,
                    headers: headers
                },
                'create': {
                    method: 'POST',
                    headers: headers
                }
            }
        );
    })


    .factory('Transltr', function($resource) {
        var headers = {
            "Content-Type": "application/json"
        };

        return $resource(
            'http://www.transltr.org/api/getlanguagesfortranslate',
            {},
            {
                'query': {
                    method: 'GET',
                    isArray: true,
                    headers: headers
                }
            }
        );
    })
