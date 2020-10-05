// 座號選擇
var students = []
$.each(temp_students, function (index, value) {
    // students.push(value.fields.seat_number + ':' + value.fields.name + " |" + value.pk);
    students.push({
        label: value.fields.seat_number + ':' + value.fields.name,
        value: value.pk
    })
});
$("#input_student_autocomp").autocomplete({
    source: students,
    select: function (event, ui) {
        $("#student").text(ui.item.label);
        $("#student").css("visibility", "visible");
        $("#input_student_autocomp").css("color", "white");
        // return false;
    }
});

// 志願選擇
$(function () {
    $("#list").sortable({
        connectWith: ".connectedSortable"
    }).disableSelection();
    $('#input_student_autocomp').on('click', function () {
        $('#assign_status').css('color', 'white');
        $("#input_student_autocomp").css("color", "black");
        $('#input_student_autocomp').val('');
    });
});

function updateOrder(arry) {
    let student = $('#input_student_autocomp').val();
    student = student.substring(student.indexOf('|') + 1);
    $.post('/course_record/', {
        'student': student,
        'order': arry
    }).done(function (msg) {
        if (msg == 'ok') {
            $('#assign_status').css('color', 'gray');
        } else if (msg == 'assigned') {
            $('#assign_status').css('color', 'gray');
        }
    });
}

function submit() {
    var idsInOrder = $("#list").sortable("toArray");
    updateOrder(idsInOrder);
    console.log(idsInOrder)
}
// 標記選取班級
$(function () {
    setActived();
});

function setActived() {
    let path = window.location.pathname.substring(1);
    $('#class_code_' + path).addClass('active');
}

