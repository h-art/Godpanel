$(function () {
  var allocationModal = $('#allocation-modal');

  window.godpanel = $('#calendar').fullCalendar({
    schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
    aspectRatio: 2.5,
    resourceLabelText: 'Risorse',
    defaultView: 'timelineMonth',
    defaultDate: new Date(),
    events: 'allocations',
    resources: 'employees',
    weekends: false,
    lang: 'it',
    customButtons: {
      myCustomButton: {
        text: '+ allocazione',
        click: function () {
          allocationModal
            .modal({show: true})
            .on('shown.bs.modal', function () {
              $(this).find('iframe').attr('src', location.protocol + '//' + location.host + '/admin/panel/allocation/add');
            })
            .on('hidden.bs.modal', function () {
              godpanel.fullCalendar('refetchEvents');
            });
        }
      }
    },
    header: {
      left: 'myCustomButton',
      center: 'title'
    },
    eventRender: function (event, element, view) {
      element.find('.fc-title').append(' (' + event.saturation + '%)');
      element.find('.fc-time').remove();
      element.on('click', function(e) {
        allocationModal
          .modal({show: true})
          .on('shown.bs.modal', function () {
            $(this).find('iframe').attr('src', location.protocol + '//' + location.host + '/admin/panel/allocation/' + event.id + '/change');
          })
          .on('hidden.bs.modal', function () {
            godpanel.fullCalendar('refetchEvents');
          });
      }),
      element.qtip({
        content: {
          text: '<strong>' + event.allocation_type + '</strong><br>'
                + 'Cliente: ' + event.client + '<br>'
                + 'Progetto: ' + event.title + '<br>'
                + 'Saturazione: ' + event.saturation + '<br>'
                + 'Inizio: ' + moment(event.start).format('DD/MM/YYYY') + '<br>'
                + 'Fine: ' + moment(event.end).format('DD/MM/YYYY')
        },
        position: {
          target: 'mouse',
          adjust: {
            mouse: false  // Can be omitted (e.g. default behaviour)
          }
        }
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
      }
    },
    resourceRender: function (resourceObj, labelTds, bodyTds) {
      labelTds
        .find('.fc-cell-text')
        .append(' <small>(' + [resourceObj.area, resourceObj.role].join(', ') + ')</small>');
    }
  });
});
