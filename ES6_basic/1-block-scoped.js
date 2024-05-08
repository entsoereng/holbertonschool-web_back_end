export default function taskBlock(trueOrFalse) {
  var task = false;
  let task2 = false;

  if (trueOrFalse) {
    var task = true;
    let task2 = true;
  }

  return [task, task2];
}
