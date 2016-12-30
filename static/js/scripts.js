$(document).ready(function() {
    $('[data-toggle="tooltip"]').tooltip();
    $('[data-toggle="popover"]').popover()

    $("#recommend_form").submit(function(event) {
        var const_value = $("#id_const").val();
        var valid_note = $("#id_note").val().length < 120;
        var nick_field = $("#id_nick");
        var regex = /(tt\d{7})[^\d]*/;
        var valid_const = regex.exec(const_value)[1];

        if (valid_const && valid_note) {
            $("#id_const").val(valid_const);
            if (!nick_field.length || (nick_field.val().length > 2)) {
                return true;
            }
        }
        return false;
    });

    $('body').on('click', 'button[name="fav"], button[name="unfav"], button[name="watch"], button[name="unwatch"]', function() {
        var data = {'const': $(this).val()};
        var btnName = $(this).attr('name');
        data[btnName] = btnName;
        ajax_request(data);

        var btn = buttons[btnName];
        $(this).removeClass(btn.class).addClass(btn.afterClass);
        $(this).attr('name', btn.afterName);
        $(this).html(btn.afterText);
    });





    if ($('div').is('#favouritePage')) {
        var pathArray = window.location.pathname.split('/');
        var path_username = pathArray[pathArray.length - 3];
        if (path_username == request_username) {
            sortable();
        }
    }

    $('input.filter_results').on('change', function() {
       $('input.filter_results').not(this).prop('checked', false);
    });

    // when on title page you click 1 of 10 stars
    $('input[name="rating"').change(function() {
        $("#star_rating_form").submit();
//        ajax_request({'value': this.value, 'checkbox': $('input[name="insert_as_new"').val()}, true);
    });
});

function sortable() {
    $('#sortable').sortable({
        placeholder: 'sort-placeholder',
        axis: 'y',
        update: function (event, ui) {
            var ordering = $(this).sortable('serialize');
            $(this).find('li').each(function(i){
                $(this).find('p#item-order').text(i+1);
            });
            ajax_request({'item_order': ordering});
        }
    });
    $("#sortable").disableSelection();
}

function ajax_request(data, refresh=false) {
    data['csrfmiddlewaretoken'] = csrftoken; // attach csrf token
    var url = [location.protocol, '//', location.host, location.pathname].join('');
    $.ajax({
        data: data,
        type: 'POST',
        url: url,
        success: function() {
//            if (refresh) {
//                window.location.reload(false);
//            }
        }
    });
}

var csrftoken = getCookie('csrftoken');
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var buttons = {
    'fav': {
        'class': 'watch-btn',
        'afterClass': 'unwatch-btn',
        'afterName': 'unfav',
        'afterText': 'unfavourite',
    },
    'unfav': {
        'class': 'unwatch-btn',
        'afterClass': 'watch-btn',
        'afterName': 'fav',
        'afterText': 'favourite',
    },
    'watch': {
        'class': 'watch-btn',
        'afterClass': 'unwatch-btn',
        'afterName': 'unwatch',
        'afterText': 'Don\'t want to see again',
    },
    'unwatch': {
        'class': 'unwatch-btn',
        'afterClass': 'watch-btn',
        'afterName': 'watch',
        'afterText': 'Want to see again',
    }
}