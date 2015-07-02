function validBraces(braces){
  braces = braces.split("");
  
  var bracketStack = [];
  for (i = 0; i < braces.length; i++)
  {
    if (braces[i] == "(") bracketStack.push("(");
    if (braces[i] == "{") bracketStack.push("{");
    if (braces[i] == "[") bracketStack.push("[");
    lastOpen = bracketStack[bracketStack.length - 1];
    if (braces[i] == ")" && lastOpen != "(") return false;
    if (braces[i] == "}" && lastOpen != "{") return false;
    if (braces[i] == "]" && lastOpen != "[") return false;
    if (")}]".indexOf(braces[i]) !== -1) bracketStack.pop();
    //bracketStack.push
  }
  if (bracketStack.length > 0) return false;
  return true;
}
