angular.module('translationApp', [
    'ui.router',
    'ngResource',

    'translationApp.services',
    'translationApp.controllers'
])
    .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider) {
        // Force angular to use square brackets for template tag
        // The alternative is using {% verbatim %}
        $interpolateProvider.startSymbol('[[').endSymbol(']]');

        // CSRF Support
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        // It makes dealing with Django slashes at the end of everything easier.
        $resourceProvider.defaults.stripTrailingSlashes = false;

        // Routing

        $urlRouterProvider.otherwise('/');
        $stateProvider
            .state(
                'translate',
                {
                    url: '/',
                    templateUrl: 'static/translation/partials/translate.html',
                    controller: 'TranslateCtrl',
                }
            )
            .state(
                'history',
                {
                    url: '/history',
                    templateUrl: 'static/translation/partials/history.html',
                    controller: 'HistoryCtrl',
                }
            )
    });
