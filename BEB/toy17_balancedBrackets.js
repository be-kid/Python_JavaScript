const balancedBrackets = function (str) {
  const stack = [];

  for (let elem of str) {
    if ("({[".includes(elem)) {
      stack.push(elem);
    } else if (")}]".includes(elem)) {
      if (stack.length === 0) {
        return false;
      } else {
        const top = stack.pop();
        if (top === "(" && elem !== ")") {
          return false;
        } else if (top === "{" && elem !== "}") {
          return false;
        } else if (top === "[" && elem !== "]") {
          return false;
        }
      }
    }
  }
  if (stack.length !== 0) {
    return false;
  }
  return true;
};

let output = balancedBrackets("[](){}");
console.log(output); // --> true

output = balancedBrackets("[({})]");
console.log(output); // --> true

output = balancedBrackets("[(]{)}");
console.log(output); // --> false
