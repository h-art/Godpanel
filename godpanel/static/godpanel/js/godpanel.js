(function ($) {
  $.fn.serializeObject = function() {
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
      if (o[this.name] !== undefined) {
        if (!o[this.name].push) {
          o[this.name] = [o[this.name]];
        }
        o[this.name].push(this.value || '');
      } else {
        o[this.name] = this.value || '';
      }
    });
    return o;
  };
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
  function updateEvent(data, method='put') {
    jQuery.ajax({
      url: 'allocations/',
      headers: { 'X-CSRFToken': getCookie('csrftoken') },
      data: JSON.stringify(data),
      dataType: 'json',
      contentType: 'application/json; charset=utf-8',
      method: method,
    }).done(function (data, textStatus, jqXHR) {
      // success, close the modal
      allocationModal.modal('hide');
    }).fail(function (data, textStatus, jqXHR) {
      if (data.responseJSON) {
        var allocationForm = $('#allocation-form');

        // clear previous errors if any
        allocationForm
          .find('.form-group')
          .each(function (i, el) {
            $(el).removeClass('has-error')
          });

        // look for errors in response and set bootstrap class
        for (key in data.responseJSON) {
          allocationForm
            .find('#id_' + key)
            .parent()
            .addClass('has-error');
        }
      }
      console.log(data, textStatus);
    });
  }

  var allocationModal = $('#allocation-modal');

  allocationModal.on('submit', '#allocation-form', function(e) {
    e.preventDefault();

    var form_method = $(this).attr('method');

    var data = $(this).serializeObject(),
        allocationId = allocationModal.attr('data-allocation-id');

    data.id = allocationId;

    updateEvent(data, form_method);

    return false;
  });

  // handle what happens when the allocation modal is opened
  allocationModal.on('show.bs.modal', function(e) {
    var qsParams = '?',
        allocationId = $(this).attr('data-allocation-id');

    if (allocationId) {
      qsParams += 'allocation=' + allocationId;
    }
    else {
      qsParams += 'new_allocation&resource_id=';
      qsParams += allocationModal.attr('data-resource-id');
      qsParams += '&start=';
      qsParams += allocationModal.attr('data-start');
    }

    $(e.target).find('.modal-body').load('allocations/form/' + qsParams);
  }).on('shown.bs.modal', function(e) {
    $(this).find('.date').datepicker({
      dateFormat: 'yy-mm-dd'
    });
  }).on('hidden.bs.modal', function () {
    $(this).removeAttr('data-allocation-id');
    $(this).removeAttr('data-resource-id');
    $(this).removeAttr('data-start');
    // refresh the calendar every time a modal is closed
    godpanel.fullCalendar('refetchEvents');
  });

  window.godpanel = $('#calendar').fullCalendar({
    schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
    aspectRatio: 2.5,
    resourceLabelText: 'Risorse',
    defaultView: 'timelineMonth',
    defaultDate: new Date(),
    editable: true,
    eventDrop: function (event, jsEvent, ui, view) {
      updateEvent({
        id: event.id,
        start: event.start.format('YYYY-MM-DD'),
        end: event.end.format('YYYY-MM-DD'),
        employee: event.resourceId,
        project: event.project_id,
        saturation: event.saturation,
        allocation_type: event.allocation_type
      });
    },
    eventResize: function (event, jsEvent, ui, view) {
      updateEvent({
        id: event.id,
        start: event.start.format('YYYY-MM-DD'),
        end: event.end.format('YYYY-MM-DD'),
        employee: event.resourceId,
        project: event.project_id,
        saturation: event.saturation,
        allocation_type: event.allocation_type
      });
    },
    events: 'allocations/',
    resources: 'employees/',
    weekends: false,
    lang: 'it',

    dayRender: function (date, cell) {
      // check closing days
      for (var i = 0; i < closing_days.length; i++) {
        if (date.format('YYYY-MM-DD') == closing_days[i]) {
          $(cell).css('background', '#EEE');
        }
      }
    },

    dayClick: function (date, jsEvent, view, resourceObj) {
      allocationModal.attr('data-resource-id', resourceObj.id);
      allocationModal.attr('data-start', date.format('YYYY-MM-DD'));
      allocationModal.modal();
    },

    header: {
      left: 'addAllocationButton',
      center: 'title'
    },

    eventRender: function (event, element, view) {
      event.note = (event.note) ? event.note : '-'; // tweak event note
      element.find('.fc-title').append(' (' + event.saturation + '%)');
      element.find('.fc-time').remove();

      // handle click on an existing event
      element.on('click', function(e) {
        allocationModal.attr('data-allocation-id', event.id);
        allocationModal.modal({show: true})
      });

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
        case 'off_request':
          element.css({
            'background': 'orange',
            'color': 'black'
          });
          break;
        case 'off':
          element.css({
            'background': 'blue',
            'color': 'white'
          });
          break;
      }
    },

    resourceRender: function (resourceObj, labelTds, bodyTds) {
      labelTds
        .find('.fc-cell-text')
        .append(' <small>(' + [resourceObj.area, resourceObj.role].join(', ') + ')</small>');
    }
  });
}(jQuery));
