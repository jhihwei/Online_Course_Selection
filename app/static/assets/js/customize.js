// Drag and Down
var dragSrcEl = null;

function handleDragStart(e) {
    this.style.opacity = '0.4';

    dragSrcEl = this;

    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/html', this.innerHTML);
    e.dataTransfer.setData('text/text', 'id');
}

function handleDragOver(e) {
    if (e.preventDefault) {
        e.preventDefault(); // Necessary. Allows us to drop.
    }

    e.dataTransfer.dropEffect = 'move'; // See the section on the DataTransfer object.

    return false;
}

function handleDragEnter(e) {
    // this / e.target is the current hover target.
    this.classList.add('over');
}

function handleDragLeave(e) {
    this.classList.remove('over'); // this / e.target is previous target element.
}

function handleDrop(e) {
    // this / e.target is current target element.

    if (e.stopPropagation) {
        e.stopPropagation(); // stops the browser from redirecting.
    }

    // Don't do anything if dropping the same column we're dragging.
    if (dragSrcEl != this) {
        // Set the source column's HTML to the HTML of the column we dropped on.
        dragSrcEl.innerHTML = this.innerHTML;
        this.innerHTML = e.dataTransfer.getData('text/html');
        console.log(e.dataTransfer.getData('text/text'));
    }

    return false;

    return false;
}

function handleDragEnd(e) {
    // this/e.target is the source node.

    [].forEach.call(items, function (item) {
        item.style.opacity = '1';
        item.classList.remove('over');
    });
}

var items = document.querySelectorAll('#list .item');
[].forEach.call(items, function (item) {
    item.addEventListener('dragstart', handleDragStart, false);
    item.addEventListener('dragenter', handleDragEnter, false);
    item.addEventListener('dragover', handleDragOver, false);
    item.addEventListener('dragleave', handleDragLeave, false);
    item.addEventListener('drop', handleDrop, false);
    item.addEventListener('dragend', handleDragEnd, false);
});
// 座號選擇
var students = []
$.each(temp_students, function(index, value){
    students.push(value.fields.seat_number + ':' + value.fields.name)
});
$("#input_student_autocomp").autocomplete({
    source: students
});