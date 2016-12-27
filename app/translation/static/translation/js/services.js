angular.module('translationApp.services', ['ngResource'])
    .factory('Translation', function($resource) {
        var headers = {
            "Content-Type": "application/json"
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
