var TipoEventoScript = function () {

    var tipoevento;
    tipoevento = function () {

        function initInput(){
            $("#id_type_tipoevento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_type_tipoevento-error").remove();
            $("#id_type_tipoevento").maxlength({limitReachedClass: "label label-danger",threshold: 5});
            $("#id_frecuencia_tipoevento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_frecuencia_tipoevento").select2({placeholder: "Seleccione Frecuencia...",allowClear: true,escapeMarkup: function (m) {return m;}});
            $("#id_frecuencia_tipoevento-error").remove();
            
        };
        initInput();

        $('#close').click(function () {
            $('#cancelar').click();
        });

        $('#cancelar').click(function () {
            initInput();
        });

        function restoreRow(oTable, nRow) {
            var aData = oTable.fnGetData(nRow);
            var jqTds = $('>td', nRow);

            for (var i = 0, iLen = jqTds.length; i < iLen; i++) {
                oTable.fnUpdate(aData[i], nRow, i, false);
            }

            oTable.fnDraw();
        }

        function editRow(oTable, nRow) {
            var aData = oTable.fnGetData(nRow);
            var jqTds = $('>td', nRow);

            jqTds[1].innerHTML = '<input type="text" class="form-control input-large" value="' + aData[1] + '" required="">';
            jqTds[3].innerHTML = '' + 
            '<a class="edit btn default btn-xs green" href=""> Salvar</a> <a class="cancel btn default btn-xs red" href=""> Cancelar</a>';
        }

        function addRow(oTable, nRow) {
            var aData = oTable.fnGetData(nRow);
            var jqTds = $('>td', nRow);
            jqTds[1].innerHTML = aData[1];
            jqTds[3].innerHTML = '' + 
            '<a class="edit btn default btn-xs purple" href="javascript:;"> Editar</a> ' +
                '<a href="#myModal' + aData[0] + '" role="button" class="btn default btn-xs black" data-toggle="modal"> Borrar</a>' +
                '<div id="myModal' + aData[0] + '" class="modal fade bs-modal-sm" tabindex="-1" role="dialog" aria-labelledby="myModalLabel3" aria-hidden="true">' +
                '<div class="modal-dialog modal-sm">' +
                '<div class="modal-content">' +
                '<div class="modal-header">' +
                '<button type="button" class="close" data-dismiss="modal" aria-hidden="true"></button>' +
                '<h4 class="modal-title">Confirmar </h4>' +
                '</div>' +
                '<div class="modal-body">' +
                '<p class="text-center">' +
                'Seguro desea borrar el TipoEvento' +
                '</p>' +
                '</div>' +
                '<div class="modal-footer">' +
                '<button class="btn default" data-dismiss="modal" aria-hidden="true">' +
                'Cancelar' +
                '</button>' +
                '<button data-dismiss="modal" class="delete btn blue">' +
                'Confirmar' +
                '</button>' +
                '</div>' +
                '</div>' +
                '</div>' +
                '</div>';
        }

        function saveRow(oTable, nRow) {
            var jqInputs = $('input', nRow);
            var aData = oTable.fnGetData(nRow);

            if(jqInputs[0].value == ''){
                alert_error('Campo no puede ser nulo');
                jqInputs[0].value(aData[1]);
                return;
            }

            $.post('/dpv_events/update_tipoevento/', {
                'id': aData[0],
                'type_tipoevento': jqInputs[0].value,
                
            }, function (data) {
                oTable.fnUpdate([data.id, data.type,data.frecuencia, '<a class="edit btn default btn-xs purple" href="javascript:;"> Editar</a> ' +
                    '<a href="#myModal' + data.id + '" role="button" class="btn default btn-xs black" data-toggle="modal"> Borrar</a>' +
                    '<div id="myModal' + data.id + '" class="modal fade bs-modal-sm" tabindex="-1" role="dialog" aria-labelledby="myModalLabel3" aria-hidden="true">' +
                    '<div class="modal-dialog modal-sm">' +
                    '<div class="modal-content">' +
                    '<div class="modal-header">' +
                    '<button type="button" class="close" data-dismiss="modal" aria-hidden="true"></button>' +
                    '<h4 class="modal-title">Confirmar </h4>' +
                    '</div>' +
                    '<div class="modal-body">' +
                    '<p class="text-center">' +
                    'Seguro desea borrar el TipoEvento' +
                    '</p>' +
                    '</div>' +
                    '<div class="modal-footer">' +
                    '<button class="btn default" data-dismiss="modal" aria-hidden="true">' +
                    'Cancelar' +
                    '</button>' +
                    '<button data-dismiss="modal" class="delete btn blue">' +
                    'Confirmar' +
                    '</button>' +
                    '</div>' +
                    '</div>' +
                    '</div>' +
                    '</div>'], nRow);
                oTable.fnDraw();
            }, 'json');
        }

        var form = $('#newtipoevento_form');

        form.validate({
            doNotHideMessage: true,
            errorElement: 'span',
            errorClass: 'help-block help-block-error',
            focusInvalid: false,

            rules: {
                type_tipoevento: {required: true,},
                frecuencia_tipoevento: {required: false,},
                
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

                var formData = new FormData($("#newtipoevento_form")[0]);

                $.ajax({
                    type: "POST",
                    url: "/dpv_events/create_tipoevento/",
                    data: formData,
                    contentType: false,
                    processData: false,
                    success: function (data) {

                        if (data.isfirst) {
                            $('#cancelar').click();
                            alert_success('Se Ha Agregado Un Nuevo Tipo De Evento.');
                            setTimeout(function() {
                                $(location).attr('href',"");
                            }, 1250);
                            return;
                        }

                        var aiNew = oTable.fnAddData([data.id, data.type,data.frecuencia, '']);
                        var nRow = oTable.fnGetNodes(aiNew[0]);
                        addRow(oTable, nRow);
                        $('#cancelar').click();
                        alert_success('Se Ha Agregado Un Nuevo TipoEvento.');
                    },
                });

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

            "order": [
                [0, "asc"]
            ],
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

        var nEditing = null;
        var nNew = false;
        $('#print').click(function () {
            $('#ToolTables_sample_editable_1_3').click();
        });

        table.on('click', '.delete', function (e) {
            e.preventDefault();

            var nRow = $(this).parents('tr')[0];
            var aData = oTable.fnGetData(nRow);
            $.post('/dpv_events/delete_tipoevento/', {
                'id': aData[0]
            }, function (data) {
                if (data.iserror) {
                    alert_error('No Se Pudo Ejecutar La Acción.');
                    return;
                }
                oTable.fnDeleteRow(nRow);
                var count = oTable.fnGetNodes().length;
                if(count == 0){
                    $('#tipoevento-body').html('<div class="no-result theme-font"> No hay Tipos de Eventos </div>');
                }

            }, 'json');
        });

        table.on('click', '.cancel', function (e) {
            e.preventDefault();
            if (nNew) {
                addRow(oTable, nEditing);
                nEditing = null;
                nNew = false;
            } else {
                addRow(oTable, nEditing);
                nEditing = null;
            }
        });

        table.on('click', '.edit', function (e) {
            e.preventDefault();

            var nRow = $(this).parents('tr')[0];

            if (nEditing !== null && nEditing != nRow) {
                restoreRow(oTable, nEditing);
                editRow(oTable, nRow);
                nEditing = nRow;
            } else if (nEditing == nRow && this.innerHTML == ' Salvar') {
                saveRow(oTable, nEditing);
                nEditing = null;
            } else {
                editRow(oTable, nRow);
                nEditing = nRow;
            }
        });

    };

    return {

        init: function () {
            tipoevento();
        }

    };

}();