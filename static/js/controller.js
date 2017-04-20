
/* Set up shit that I barely understand */
var ISSChatApp = angular.module('ISSChatApp', []);

ISSChatApp.controller('ChatController', function($scope)
{
    
    var socket = io.connect('https://' + document.domain + ':8080');


    $scope.queries = [];
 


    /* Displaying the results of a query */
    socket.on('displayactors1', function(results)
    {
        console.log('We made it in displayactors1');
        console.log(results);
        $scope.queries.push(results);
        $scope.$apply();
        var elem = document.getElementById('querylist');
        elem.scrollTop = elem.scrollHeight;

    });

    socket.on('displayactors2', function(results)
    {
        
        console.log(results);
        $scope.queries.push(results);
        $scope.$apply();
        var elem = document.getElementById('querylist');
        elem.scrollTop = elem.scrollHeight;
    });

    socket.on('displaymovies', function(results)
    {
        
        console.log(results);
        $scope.queries.push(results);
        $scope.$apply();
        var elem = document.getElementById('querylist');
        elem.scrollTop = elem.scrollHeight;
   
   
    });


    /* Searching for a specific user */
    $scope.search = function search()
    {
        console.log('Searching for ', $scope.query);
        socket.emit('search', $scope.query);
    };

});