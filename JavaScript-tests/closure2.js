/*===============(type-1)========================*/

func_para=25;
function acceptFunctionArg(thisIsActuallyAFunction)
{
thisIsActuallyAFunction(func_para);
}

acceptFunctionArg(function(func_para)
{

console.log(func_para);

});

/*===============(type-2)========================*/

func_para2=50;
acceptFunctionArg = function(thisIsActuallyAFunction)
{
thisIsActuallyAFunction(func_para2);
}

acceptFunctionArg(function(func_para2)
{

console.log(func_para2);

});