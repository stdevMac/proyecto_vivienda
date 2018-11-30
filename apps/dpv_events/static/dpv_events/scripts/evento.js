var EventoScript = function () {

    var evento;
    evento = function () {

        var tableTema = $('#table_1');
        var tableThemes = $('#table_themes');
        var tableThemesSugeridos = $('#table_themes_sugeridos');
        var temas = [];
        var inform = $('#tab_1_1');
        var infoacta = $('#tab_1_2');
        var tableAcuerdos = $('#table_2');

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

            // borrar la fila de la tabla
        }

        function setInput() {
            $("#id_type_evento").val(model.type).closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_type_evento").select2({placeholder: "Seleccione el Evento...",allowClear: true,escapeMarkup: function (m) {return m;}});
            $("#id_type_evento-error").remove();
            $("#id_date_programed_evento").val(model.date_programed).closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_date_programed_evento-error").remove();
            $("#id_site_evento").val(model.site).closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_site_evento-error").remove();
            $("#id_site_evento").maxlength({limitReachedClass: "label label-danger",threshold: 5});
            $("#id_month_evento").val(model.month).closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_month_evento").select2({placeholder: "Seleccione el Mes...",allowClear: true,escapeMarkup: function (m) {return m;}});
            $("#id_month_evento-error").remove();
            var is_extraordinario = model.is_extraordinario ? $("#id_is_extraordinario_evento").attr("checked", true).parent().addClass("checked") : $("#id_is_extraordinario_evento").attr("checked", false).parent().removeClass("checked");
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

            tableTema.find('.delete').each(function(){
                $(this).click();
            });

            for(theme of model.themes){
                addTema(theme.id,theme.asunto,theme.responsable_id,theme.responsable_name)
            }

        }
        setInput();

        function initTheme() {
            $("#id_asunto_tema_evento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_asunto_tema_evento-error").remove();
            $("#id_asunto_tema_evento").maxlength({limitReachedClass: "label label-danger",threshold: 5});
            $("#id_responsable_tema_evento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_responsable_tema_evento").select2({placeholder: "Seleccione el Responsable...",allowClear: true,escapeMarkup: function (m) {return m;}});
            $("#id_responsable_tema_evento-error").remove();
        }
        initTheme();

        function initThemeSugerido() {
            $("#id_asunto_tema_sugerido_evento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_asunto_tema_sugerido_evento-error").remove();
            $("#id_asunto_tema_sugerido_evento").maxlength({limitReachedClass: "label label-danger",threshold: 5});
        }
        initThemeSugerido();

        function initActa() {
            $("#id_body_acta_evento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_body_acta_evento-error").remove();
        }
        initActa();

        function initAcuerdo() {
            $("#id_asunto_acuerdo_evento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_asunto_acuerdo_evento-error").remove();
            $("#id_asunto_acuerdo_evento").maxlength({limitReachedClass: "label label-danger",threshold: 5});
            $("#id_date_finish_acuerdo_evento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $("#id_date_finish_acuerdo_evento-error").remove();
            $("#id_responsables_acuerdo_evento").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            $('#id_responsables_acuerdo_evento').select2({
                placeholder: "Seleccione los Responsables",
                allowClear: true
            });
            $("#id_responsables_acuerdo_evento-error").remove();

            $('.todo-taskbody-due').datepicker({
                rtl: Metronic.isRTL(),
                format: 'yyyy-mm-dd',
                orientation: "left",
                autoclose: true,
                language: "es",
            });
        }
        initAcuerdo();

        $('#cancelar').click(function () {
            $('#to_info_evento').click();
        });

        $('#close_theme_event').click(function () {
            $('#cancelar_theme_event').click();
        });

        $('#cancelar_theme_event').click(function () {
            initTheme();
        });

        $('#close_theme_sugerido').click(function () {
            $('#cancelar_theme_sugerido').click();
        });

        $('#cancelar_theme_sugerido').click(function () {
            initThemeSugerido();
        });

        $('#close_acta_evento').click(function () {
            $('#cancelar_acta_evento').click();
        });

        $('#cancelar_acta_evento').click(function () {
            initActa();
        });

        $('#close_acuerdo_evento').click(function () {
            $('#cancelar_acuerdo_evento').click();
        });

        $('#cancelar_acuerdo_evento').click(function () {
            initAcuerdo();
        });

        $('#to_info_evento').click(function () {

            setInput();
            initTheme();

        });

        var form = $('#editevento_form');

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

                var formData = new FormData($("#editevento_form")[0]);
                formData.append("id",model.id);

                for(var i = 0; i < temas.length;i++){
                    formData.append("temas[" + i + "][asunto]",temas[i].asunto);
                    formData.append("temas[" + i + "][responsable_id]",temas[i].responsable_id);
                }

                $.ajax({
                    type: "POST",
                    url: "/dpv_events/update_evento/",
                    data: formData,
                    contentType: false,
                    processData: false,
                    success: function (data) {
                        model.set(data.event);

                        inform.find('.type_evento').each(function () {
                            $(this).html(data.event.type.type.toUpperCase());
                        });
                        // PONER EL FORMATO BIEN
                        inform.find('.date_programed_evento').each(function () {
                            $(this).html(data.event.get_date_programed);
                        });

                        inform.find('.time_programed_evento').each(function () {
                            $(this).html(data.event.time_programed);
                        });
                        // FIN DEL FORMATO QUE NECESITO
                        inform.find('.site_evento').each(function () {
                            $(this).html(data.event.site.toUpperCase());
                        });

                        inform.find('.month_evento').each(function () {
                            $(this).html(data.event.get_month.toUpperCase());
                        });

                        inform.find('.is_extraordinario_evento').each(function () {
                            $(this).html(data.event.get_is_extraordinario.toUpperCase());
                        });

                        tableThemes.html('');
                        for(theme of model.themes){
                            tableThemes.append('<tr><td>' + theme.id + '</td><td>' + theme.asunto + '</td><td>' + theme.responsable_name + '</td></tr>');
                        }

                        $('#to_info_evento').click();
                        alert_success('Se Ha Modificado Exitosamente El Evento.');
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

        var form_tema_sugerido = $('#newtheme_sugerido_form');

        form_tema_sugerido.validate({
            doNotHideMessage: true,
            errorElement: 'span',
            errorClass: 'help-block help-block-error',
            focusInvalid: false,

            rules: {
                asunto_tema_sugerido_evento: {
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

                var formData = new FormData($("#newtheme_sugerido_form")[0]);
                formData.append("event_id",model.id);

                $.ajax({
                    type: "POST",
                    url: "/dpv_events/create_temaevento/",
                    data: formData,
                    contentType: false,
                    processData: false,
                    success: function(data){
                        if(data.isfirst){
                            tableThemesSugeridos.find('tbody').html('');
                        }
                        var count = tableThemesSugeridos.find('tbody').find('tr').length + 1;
                        $('#cantidad_temas_sugeridos').html(count);
                        tableThemesSugeridos.append('<tr><td>' + count + '</td><td>' + data.asunto + '</td><td>' + data.responsable_name + '</td><td><button type="button" class="btn green btn-xs tooltips done" data-theme="' + data.id + '"><i class="icon-check"></i> Aprobar</button></td></tr>');
                        $('#cancelar_theme_sugerido').click();
                        alert_success('Se Ha Creado Exitosamente El Tema Para Sugerir.');
                    }
                });

            }

        });

        var form_acta_evento = $('#newacta_evento_form');

        form_acta_evento.validate({
            doNotHideMessage: true,
            errorElement: 'span',
            errorClass: 'help-block help-block-error',
            focusInvalid: false,

            rules: {
                body_acta_evento: {
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

                var formData = new FormData($("#newacta_evento_form")[0]);
                formData.append("event_id",model.id);

                $.ajax({
                    type: "POST",
                    url: "/dpv_events/create_acta/",
                    data: formData,
                    contentType: false,
                    processData: false,
                    success: function(data){
                        infoacta.find('.portlet').removeClass('hidden');
                        infoacta.find('.code_acta_evento').each(function () {
                            $(this).html(data.code);
                        });
                        infoacta.find('.body_acta_evento').each(function () {
                            $(this).html(data.body);
                        });
                        $('#to_create_acta').addClass('hidden');
                        $('#cancelar_acta_evento').click();
                        alert_success('Se Ha Creado Exitosamente El Acta Para Este Evento.');
                    }
                });

            }

        });

        var form_acuerdo_evento = $('#newacuerdo_evento_form');

        form_acuerdo_evento.validate({
            doNotHideMessage: true,
            errorElement: 'span',
            errorClass: 'help-block help-block-error',
            focusInvalid: false,

            rules: {
                asunto_acuerdo_evento: {
                    required: true
                },
                date_finish_acuerdo_evento: {
                    required: true
                },
                responsables_acuerdo_evento: {
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

                var formData = new FormData($("#newacuerdo_evento_form")[0]);
                formData.append("event_id",model.id);

                $.ajax({
                    type: "POST",
                    url: "/dpv_events/create_acuerdo/",
                    data: formData,
                    contentType: false,
                    processData: false,
                    success: function(data){

                        if(data.isfirst){
                            $('#cancelar_acuerdo_evento').click();
                            alert_success('Se Ha Creado Exitosamente El Acuerdo Para Este Evento.');
                            setTimeout(function() {
                                $(location).attr('href',"");
                            }, 1250);
                            return;
                        }
                        tableAcuerdos.append('<tr><td>' + data.code + '</td><td>' + data.asunto + '</td><td>' + data.responsables + '</td><td>' + data.date_finish + '</td><td>' + data.state + '</td><td></td></tr>');
                        $('#cancelar_acuerdo_evento').click();
                        alert_success('Se Ha Creado Exitosamente El Acuerdo Para Este Evento.');
                    }
                });

            }

        });

        tableTema.on('click', '.delete', function (e) {
            e.preventDefault();

            var nRow = $(this).parents('tr')[0];
            delTema($(this).attr('data-tema'));
            nRow.remove();

        });

        tableThemesSugeridos.on('click', '.done', function (e) {

            var input = $(this);

            $.ajax({
                type: "POST",
                url: "/dpv_events/aprobar_temaevento/",
                data: {"theme_id":input.attr('data-theme')},
                success: function(data){
                    input.closest('tr').remove();
                    var count_ts = tableThemesSugeridos.find('tbody').find('tr').length;
                    var count_t = tableThemes.find('tr').length;
                    if(count_ts === 0){
                        tableThemesSugeridos.append('<tr><td colspan="4" class="text-center text-danger">SIN TEMAS SUGERIDOS</td></tr>');
                        count_ts = ''
                    }
                    $('#cantidad_temas_sugeridos').html(count_ts);
                    tableThemes.append('<tr><td>' + count_t + '</td><td>' + data.asunto + '</td><td>' + data.responsable_name + '</td></tr>')
                }
            });
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
                data: {"type_id":event.val(),"month":month.val(), "event_id": model.id},
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
            evento();
        }

    };

}();