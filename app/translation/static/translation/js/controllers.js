var translationControllers = angular.module('translationApp.controllers', []);

translationControllers.controller('TranslateCtrl', function($scope, Translation) {
    $scope.error = false;

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

});

translationControllers.controller('HistoryCtrl', function($scope, Translation) {
    $scope.error = false;
    
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

});
