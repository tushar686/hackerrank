var stack = [];
var operators = '-+*/';


function parsePrefix(expression) {
	var ele = expression[expression.length-1];
	if(expression.length === 0)
		return stack.splice(0, 1);
	if(operators.indexOf(ele) > -1) {
		evaluateExpression(ele);
	} else {
		stack.push(ele);
	}
	return parsePrefix(expression.slice(0, -1));
}

function evaluateExpression(ele) {
	var result = eval(stack.splice(stack.length-1, stack.length) + ele + stack.splice(stack.length-1, stack.length));
	stack.push(result);
}

var result = parsePrefix('* - 6 5 7'.split(' '));
console.log(result);

var result = parsePrefix("- * / 15 - 7 + 1 1 3 + 2 + 1 1".split(' '));
console.log(result);