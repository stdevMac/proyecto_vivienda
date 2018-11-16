var EventosScript = function () {

    var eventos;
    eventos = function () {

        var tableTema = $('#table_1');
        var temas = [];

        function addTema(id,asunto,responsable_id,responsable_name) {

            temas.push({
                "id": id,
                "asunto": asunto,
                "responsable_id": responsable_id,
            });

            tableTema.append('<tr>' +
                '<td>' + id + '</td>' +
                '<td>' + asunto + '</td>' +
                '<td>' + responsable_name + '</td>' +
                '<td><button class="delete btn btn-xm default" type="button" data-tema="' + id + '"><i class="icon-trash"></i></button></td>' +
                '</tr>');
        }

        function delTema(id) {
            for(var i = 0; i < temas.length; i++){
                if(temas[i].id == id){
                    temas.splice(i,1);
                }
            }
        }

        function initInput() {
            $("#id_type_evento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_type_evento").select2({placeholder: "Seleccione el Evento...",allowClear: true,escapeMarkup: function (m) {return m;}});
            $("#id_type_evento-error").remove();
            $("#id_date_programed_evento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_date_programed_evento-error").remove();
            $("#id_site_evento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_site_evento-error").remove();
            $("#id_site_evento").maxlength({limitReachedClass: "label label-danger",threshold: 5});
            $("#id_month_evento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_month_evento").select2({placeholder: "Seleccione el Mes...",allowClear: true,escapeMarkup: function (m) {return m;}});
            $("#id_month_evento-error").remove();
            $("#id_is_extraordinario_evento").attr("checked", false).parent().removeClass("checked");
            if (jQuery().datepicker) {$(".date-picker").datepicker({rtl: Metronic.isRTL(),orientation: "left", autoclose: true, language: "es"});}

            $(".form_meridian_datetime").datetimepicker({
                isRTL: Metronic.isRTL(),
                format: "yyyy-mm-dd hh:ii",
                showMeridian: true,
                autoclose: true,
                pickerPosition: (Metronic.isRTL() ? "bottom-right" : "bottom-left"),
                todayBtn: true,
                startDate: new Date(),
                language: "es",
            });
            
        }
        initInput();

        function initTheme() {
            $("#id_asunto_tema_evento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_asunto_tema_evento-error").remove();
            $("#id_asunto_tema_evento").maxlength({limitReachedClass: "label label-danger",threshold: 5});
            $("#id_responsable_tema_evento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_responsable_tema_evento").select2({placeholder: "Seleccione el Responsable...",allowClear: true,escapeMarkup: function (m) {return m;}});
            $("#id_responsable_tema_evento-error").remove();
        }
        initTheme();

        $('#cancelar').click(function () {
            $('#to_list_evento').click();
        });

        $('#close_theme_event').click(function () {
            $('#cancelar_theme_event').click();
        });

        $('#cancelar_theme_event').click(function () {
            initTheme();
        });

        $('#to_list_evento').click(function () {
            initInput();
            initTheme();

            tableTema.find('.delete').each(function(){
                $(this).click();
            });

        });

        function addRow(oTable, nRow, id) {
            var aData = oTable.fnGetData(nRow);
            var jqTds = $('>td', nRow);
            jqTds[3].innerHTML = aData[3];
            jqTds[4].innerHTML = aData[4];
            jqTds[5].innerHTML = '' +
            '<a class="edit btn default btn-xs purple" href="javascript:;"> Ver</a> ' +
                '<a href="#myModal' + id + '" role="button" class="btn default btn-xs black" data-toggle="modal"> Borrar</a>' +
                '<div id="myModal' + id + '" class="modal fade bs-modal-sm" tabindex="-1" role="dialog" aria-labelledby="myModalLabel3" aria-hidden="true">' +
                '<div class="modal-dialog modal-sm">' +
                '<div class="modal-content">' +
                '<div class="modal-header">' +
                '<button type="button" class="close" data-dismiss="modal" aria-hidden="true"></button>' +
                '<h4 class="modal-title">Confirmar </h4>' +
                '</div>' +
                '<div class="modal-body">' +
                '<p class="text-center">' +
                'Seguro desea borrar el Evento' +
                '</p>' +
                '</div>' +
                '<div class="modal-footer">' +
                '<button class="btn default" data-dismiss="modal" aria-hidden="true">' +
                'Cancelar' +
                '</button>' +
                '<button data-dismiss="modal" class="delete btn blue" data-id="' + id + '">' +
                'Confirmar' +
                '</button>' +
                '</div>' +
                '</div>' +
                '</div>' +
                '</div>';
        }

        var form = $('#newevento_form');

        form.validate({
            doNotHideMessage: true,
            errorElement: 'span',
            errorClass: 'help-block help-block-error',
            focusInvalid: false,

            rules: {
                user_evento: {required: true,},
                type_evento: {required: true,},
                date_programed_evento: {required: true,date: true},
                site_evento: {required: true,},
                month_evento: {required: true,digits: true,},
                is_extraordinario_evento: {required: false,},

            },

            errorPlacement: function (error, element) {
                error.insertAfter(element);
            },

            highlight: function (element) {
                $(element)
                    .closest('.form-group').removeClass('has-success').addClass('has-error');
            },

            unhighlight: function (element) {
                $(element)
                    .closest('.form-group').removeClass('has-error');
            },

            success: function (label, element) {
                label
                        .addClass('valid')
                        .closest('.form-group').removeClass('has-error').addClass('has-success');
            },

            submitHandler: function (form) {

                if(temas.length == 0){
                    alert_error('Debe añadir al menos otro tema.');
                    return;
                }

                var formData = new FormData($("#newevento_form")[0]);

                for(var i = 0; i < temas.length;i++){
                    formData.append("temas[" + i + "][asunto]",temas[i].asunto);
                    formData.append("temas[" + i + "][responsable_id]",temas[i].responsable_id);
                }

                $.ajax({
                    type: "POST",
                    url: "/dpv_events/create_evento/",
                    data: formData,
                    contentType: false,
                    processData: false,
                    success: function (data) {

                        if (data.isfirst) {
                            $('#cancelar').click();
                            alert_success('Se Ha Agregado Un Nuevo Evento.');
                            setTimeout(function() {
                                $(location).attr('href',"");
                            }, 1250);
                            return;
                        }

                        var aiNew = oTable.fnAddData([data.type,data.date_programed,data.site,data.month,data.is_extraordinario, '']);
                        var nRow = oTable.fnGetNodes(aiNew[0]);
                        addRow(oTable, nRow, data.id);
                        $('#to_list_evento').click();
                        alert_success('Se Ha Agregado Un Nuevo Evento.');
                    },
                });

            }

        });

        var form_tema = $('#newtheme_event_form');

        form_tema.validate({
            doNotHideMessage: true,
            errorElement: 'span',
            errorClass: 'help-block help-block-error',
            focusInvalid: false,

            rules: {
                asunto_tema_evento: {
                    required: true
                },
                responsable_tema_evento: {
                    required: true
                },
            },

            errorPlacement: function (error, element) {
                error.insertAfter(element);
            },

            highlight: function (element) {
                $(element)
                    .closest('.form-group').removeClass('has-success').addClass('has-error');
            },

            unhighlight: function (element) {
                $(element)
                    .closest('.form-group').removeClass('has-error');
            },

            success: function (label, element) {
                label
                        .addClass('valid')
                        .closest('.form-group').removeClass('has-error').addClass('has-success'); // set success class to the control group
            },

            submitHandler: function (form) {
                var id = $('#table_1 tbody').find('tr').length + 1;
                var asunto = $('#id_asunto_tema_evento').val();
                var responsable_id = $('#id_responsable_tema_evento').val();
                var responsable_name = $('#id_responsable_tema_evento').text();
                addTema(id,asunto,responsable_id,responsable_name);
                $('#cancelar_theme_event').click();
            }

        });

        var table = $('#sample_editable_1');

        $.extend(true, $.fn.DataTable.TableTools.classes, {
            "container": "btn-group tabletools-dropdown-on-portlet",
            "buttons": {
                "normal": "btn btn-sm default hidden",
                "disabled": "btn btn-sm default disabled"
            },
            "collection": {
                "container": "DTTT_dropdown dropdown-menu tabletools-dropdown-menu"
            }
        });

        var oTable = table.dataTable({

            "lengthMenu": [
                [5, 10, 20, -1],
                [5, 10, 20, "Todos"]
            ],

            "pageLength": 5,

            "language": {
                "emptyTable": "No hay datos disponibles.",
                "info": "Mostrando _START_ a _END_ de _TOTAL_ registros.",
                "infoEmpty": "Sin registros encontrados.",
                "infoFiltered": "(de un total de _MAX_ registros)",
                "lengthMenu": " _MENU_ registros",
                "search": "Buscar:",
                "zeroRecords": "No se encontraron registros."
            },
            "columnDefs": [
                {
                    'orderable': true,
                    'targets': [0]
                },
                {
                    "searchable": true,
                    "targets": [0]
                }
            ],

            "dom": "<'row' <'col-md-12'T>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r><'table-scrollable't><'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",

            "order": [],
            "tableTools": {
                "sSwfPath": "/static/config/global/plugins/datatables/extensions/TableTools/swf/copy_csv_xls_pdf.swf",
                "aButtons": [
                    {
                        "sExtends": "pdf",
                        "sButtonText": "PDF"
                    },
                    {
                        "sExtends": "csv",
                        "sButtonText": "CSV"
                    },
                    {
                        "sExtends": "xls",
                        "sButtonText": "Excel"
                    },
                    {
                        "sExtends": "print",
                        "sButtonText": "Imprimir",
                        "sInfo": 'Por favor presiona "CTR+P" para imprimir o "ESC" para salir',
                        "sMessage": "Generado por BYT"
                    }
                ]
            }
        });

        var tableWrapper = $("#sample_editable_1_wrapper");

        tableWrapper.find(".dataTables_length select").select2({
            showSearchInput: false
        });

        $('#print').click(function () {
            $('#ToolTables_sample_editable_1_3').click();
        });

        table.on('click', '.delete', function (e) {
            e.preventDefault();

            var nRow = $(this).parents('tr')[0];
            var aData = oTable.fnGetData(nRow);
            $.post('/dpv_events/delete_evento/', {
                'id': $(this).attr('data-id')
            }, function (data) {
                if (data.iserror) {
                    alert_error('No Se Pudo Ejecutar La Acción.');
                    return;
                }
                oTable.fnDeleteRow(nRow);
                var count = oTable.fnGetNodes().length;
                if(count == 0){
                    $('#evento-body').html('<div class="no-result theme-font"> No hay Eventos </div>');
                }

            }, 'json');
        });

        tableTema.on('click', '.delete', function (e) {
            e.preventDefault();

            var nRow = $(this).parents('tr')[0];
            delTema($(this).attr('data-tema'));
            nRow.remove();

        });

        function verify_event () {
            var month = $('#id_month_evento');
            var event = $('#id_type_evento');
            var is_extraordinario = $('#id_is_extraordinario_evento');

            if(event.val() === ""){
                is_extraordinario.attr("disabled", false);
                return;
            }

            if (month.val() === "") {
                is_extraordinario.attr("disabled", false);
                return;
            }

            month.attr("readonly", true).attr("disabled", true);

            $.ajax({
                type: "POST",
                url: "/dpv_events/verify_evento/",
                data: {"type_id":event.val(),"month":month.val()},
                success: function(data){
                    month.attr("readonly", false).attr("disabled", false);

                    if(data.exist){
                        info('Para El Mes Seleccionado Existe Un(a) "' + data.type + '" Ordinario.');
                        is_extraordinario.attr("checked", true).attr("disabled", true).parent().addClass("checked");
                    }
                    if(!data.exist){
                        is_extraordinario.attr("disabled", false);
                    }
                },
                error: function(jqXHR){
                    month.attr("readonly", false).attr("disabled", false).removeClass("spinner");
                }
            });
        }

        $('#id_month_evento').on('change',function(){
            verify_event();
        });

        $('#id_type_evento').on('change',function(){
            verify_event();
        });

    };

    return {

        init: function () {
            eventos();
        }

    };

}();