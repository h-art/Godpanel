$(function () {
  /**
   * Get a cookie from the browser
   * @param  {string} name The cookie name
   * @return {string}      The cookie value
   */
  function getCookie (name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');

      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  /**
   * Update an event
   * @param  {object} event The event object
   * @return void
   */
  function updateEvent (event) {
    jQuery.ajax({
      url: '/godpanel/allocations/',
      headers: { 'X-CSRFToken': getCookie('csrftoken') },
      data: JSON.stringify({
        id: event.id,
        start: event.start.format('YYYY-MM-DD'),
        end: event.end.format('YYYY-MM-DD')
      }),
      dataType: 'json',
      contentType: 'application/json; charset=utf-8',
      method: 'PUT',
    }).done(function (data, textStatus, jqXHR) {
      // Success, do nothing
    }).fail(function (data, textStatus, jqXHR) {
      alert(data.responseJSON.message);
    });
  }

  var allocationModal = $('#allocation-modal');

  window.godpanel = $('#calendar').fullCalendar({
    schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
    aspectRatio: 2.5,
    resourceLabelText: 'Risorse',
    defaultView: 'timelineMonth',
    defaultDate: new Date(),
    editable: true,
    eventDrop: function (event, jsEvent, ui, view) { updateEvent(event); },
    eventResize: function (event, jsEvent, ui, view) { updateEvent(event); },
    events: 'allocations/',
    resources: 'employees/',
    weekends: false,
    lang: 'it',
    customButtons: {
      addAllocationButton: {
        text: 'Nuova allocazione',
        click: function () {
          allocationModal
            .modal({show: true})
            .on('shown.bs.modal', function () {
              $(this).find('iframe').attr('src', location.protocol + '//' + location.host + '/admin/godpanel/allocation/add/?_popup=1');
            })
            .on('hidden.bs.modal', function () {
              godpanel.fullCalendar('refetchEvents');
            });
        }
      }
    },
    header: {
      left: 'addAllocationButton',
      center: 'title'
    },
    eventRender: function (event, element, view) {
      event.note = (event.note) ? event.note : '-'; // tweak event note.
      element.find('.fc-title').append(' (' + event.saturation + '%)');
      element.find('.fc-time').remove();
      element.on('click', function(e) {
        allocationModal
          .modal({show: true})
          .on('shown.bs.modal', function () {
            $(this).find('iframe').attr('src', location.protocol + '//' + location.host + '/admin/godpanel/allocation/' + event.id + '/change/?_popup=1');
          })
          .on('hidden.bs.modal', function () {
            godpanel.fullCalendar('refetchEvents');
          });
      });
//      element.qtip({
//        content: {
//          text: '<strong>' + event.allocation_type + '</strong><br>'
//                + 'Cliente: ' + event.client + '<br>'
//                + 'Progetto: ' + event.title + '<br>'
//                + 'Saturazione: ' + event.saturation + '<br>'
//                + 'Inizio: ' + moment(event.start).format('DD/MM/YYYY') + '<br>'
//                + 'Fine: ' + moment(event.end).format('DD/MM/YYYY') + '<br>'
//                + 'Note: ' + event.note
//        },
//        position: {
//          target: 'mouse',
//          adjust: {
//            mouse: false  // Can be omitted (e.g. default behaviour)
//          }
//        }
//      });
      switch (event.allocation_type) {
        case 'allocation':
          element.css('background', 'green');
          break;
        case 'pre-allocation':
          element.css({
            'background': 'yellow',
            'color': 'black'
          });
          break;
        case 'guess':
          element.css('background', 'red');
          break;
      }
    },
    resourceRender: function (resourceObj, labelTds, bodyTds) {
      labelTds
        .find('.fc-cell-text')
        .append(' <small>(' + [resourceObj.area, resourceObj.role].join(', ') + ')</small>');
    }
  });
});
