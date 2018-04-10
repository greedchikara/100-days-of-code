function longestSubstring(str) {
  var visited = {};
  var maxLength = 0;
  var start = 0;
  var i, j = 0;
  strLength = str.length;
  for(i = 0; i < strLength; i++) {
    if(visited[str[i]] != undefined) {
        start = Math.max(start, visited[str[i]] + 1);
    }
    visited[str[i]] = i;
    if(maxLength <= (i - start + 1)) {
        maxLength = i - start + 1;
        j = start;
        k = i;
    }
    console.log(j, k);
  }
  return str.slice(j, k+1)
}

longestSubstring("abacdjeabee")


function longestSubstring(str) {
    var maxLength = 0;
    var k, l = 0;
    for(i =0; i < str.length; i++) {
        var visited = [];
        for(j = i; i < str.length; j++) {
            if (visited.indexOf(str[j]) == -1) {
                visited.push(str[j])
                if(maxLength <= visited.length) {
                    maxLength = visited.length
                    k = i;
                    l = j;
                }
            } else {
                break;
            }
        }
    }
    return str.slice(k, l + 1)
}