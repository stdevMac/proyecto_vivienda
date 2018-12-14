var TipoEventoScript = function () {

    var tipoevento;
    tipoevento = function () {

        function initInput(){
            jQuery("#id_type_tipoevento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            jQuery("#id_type_tipoevento-error").remove();
            jQuery("#id_type_tipoevento").maxlength({limitReachedClass: "label label-danger",threshold: 5});
            jQuery("#id_frecuencia_tipoevento").val("").closest(".form-group").removeClass("has-success").closest(".form-group").removeClass("has-error");
            jQuery("#id_frecuencia_tipoevento").select2({placeholder: "Seleccione Frecuencia...",allowClear: true,escapeMarkup: function (m) {return m;}});
            jQuery("#id_frecuencia_tipoevento-error").remove();
        };
        initInput();

        jQuery('#close').click(function () {
            jQuery('#cancelar').click();
        });

        jQuery('#cancelar').click(function () {
            initInput();
        });

        var form = jQuery('#newtipoevento_form');

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
                jQuery(element)
                    .closest('.form-group').removeClass('has-success').addClass('has-error');
            },

            unhighlight: function (element) {
                jQuery(element)
                    .closest('.form-group').removeClass('has-error');
            },

            success: function (label, element) {
                label
                        .addClass('valid')
                        .closest('.form-group').removeClass('has-error').addClass('has-success');
            },

            submitHandler: function (form) {

                var formData = new FormData(jQuery("#newtipoevento_form")[0]);

                jQuery.ajax({
                    type: "POST",
                    url: "/dpv_events/create_tipoevento/",
                    data: formData,
                    contentType: false,
                    processData: false,
                    success: function (data) {

                        if (data.isfirst) {
                            jQuery('#cancelar').click();
                            alert_success('Se Ha Agregado Un Nuevo Tipo De Evento.');
                            setTimeout(function() {
                                jQuery(location).attr('href',"");
                            }, 1250);
                            return;
                        }

                        var aiNew = oTable.fnAddData([data.id, data.type,data.frecuencia, '']);
                        var nRow = oTable.fnGetNodes(aiNew[0]);
                        addRow(oTable, nRow);
                        jQuery('#cancelar').click();
                        alert_success('Se Ha Agregado Un Nuevo TipoEvento.');
                    },
                });

            }

        });

        var table = jQuery('#sample_editable_1');

    };

    return {

        init: function () {
            tipoevento();
        }

    };

}();