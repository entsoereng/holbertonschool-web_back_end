export default function taskBlock(trueOrFalse) {
  var task = true;
  let task2 = true;

  if (trueOrFalse) {
    var task = true;
    let task2 = false;
  }

  return [task, task2];
}
