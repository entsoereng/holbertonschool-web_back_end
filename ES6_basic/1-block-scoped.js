export default function taskBlock(trueOrFalse) {
  var task = false;
  let task2 = false;

  if (trueOrFalse) {
    var task = true;
    let task2 = false;
  }

  return [task, task2];
}
