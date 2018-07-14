helloWorldModule = angular.module("HelloWorld", []);
helloWorldModule.controller("HelloWorldController", function ($scope) {
    $scope.hello.greet = '鸡蛋';
    $scope.hello.response = "来一个";
})
