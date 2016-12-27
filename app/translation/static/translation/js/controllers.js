var translationControllers = angular.module('translationApp.controllers', []);

translationControllers.controller('TranslateCtrl', function($scope, Translation, Transltr) {
    $scope.error = false;
    $scope.transltrError = false;

    $scope.translate = function(text) {
        Translation.create(
            {
                "original_text": text 
            },
            function(response) {
                $scope.translation = response;
                $scope.error = false;
            },
            function(error) {
                $scope.error = true;
            }
        );
    };

    $scope.getLanguageMappings = function() {
        Transltr.query(
            function(response) {
                $scope.languageMappings = {};
                for (index in response) {
                    var pair = response[index];
                    $scope.languageMappings[pair['languageCode']] = pair['languageName'];
                }
            },
            function(error) {
                $scope.transltrError = true;
            }
        );
    };

});

translationControllers.controller('HistoryCtrl', function($scope, Translation, Transltr) {
    $scope.error = false;
    $scope.transltrError = false;
    
    $scope.listTranslations = function() {
        Translation.query(
            function(response) {
                $scope.translationList = response;
                $scope.error = false;
            },
            function(error) {
                $scope.error = true;    
            }
        );
    };

    $scope.getLanguageMappings = function() {
        Transltr.query(
            function(response) {
                $scope.languageMappings = {};
                for (index in response) {
                    var pair = response[index];
                    $scope.languageMappings[pair['languageCode']] = pair['languageName'];
                }
            },
            function(error) {
                $scope.transltrError = true;
            }
        );
    };

});
