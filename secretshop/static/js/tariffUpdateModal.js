const priceOperatorSelect = $("#tariff-update-price-operator")
const priceAmountInput = $("#tariff-update-price-value")
const priceUnitSelect = $("#tariff-update-price-unit")
const commissionOperatorSelect = $("#tariff-update-commission-operator")
const commissionAmountInput = $("#tariff-update-commission-value")
const commissionUnitSelect = $("#tariff-update-commission-unit")
const submitButton = $("#tariffs-bulk-update-submit")
const closeButton = $("#tariffs-bulk-update-close")
const alertContainer = $("#tariffs-update-alert")


async function updateTariffs(ids, commissionData, priceData) {
    const response = await fetch('/api/backend/tariff/bulk/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            ids,
            commission: commissionData,
            price: priceData
        })
    })
    
    console.log(await response.json())
}

$(document).ready(function() {
    let loading = false

    submitButton.on('click', async () => {
        if(loading) return

        const priceValue = priceAmountInput.val()
        const commissionValue = commissionAmountInput.val()
        const selectedTariffsInputs = $("input.action-select:checked")
        const tariffsList = []
        selectedTariffsInputs.each(function() {
            tariffsList.push(parseInt($(this).attr('value')));
        });

        if(!priceValue && ! commissionValue) {
            alertContainer.text("Пожалуйста, заполните, хотя бы одно значение для обновления")
            alertContainer.show(300)

            setTimeout(() => alertContainer.hide(300), 3000)
            return
        } else {
            alertContainer.hide(300)
        }

        if(!tariffsList.length) {
            alertContainer.text("Пожалуйста, выберите хотя бы один тариф для обновления")
            alertContainer.show(300)

            setTimeout(() => alertContainer.hide(300), 3000)
            return
        } else {
            alertContainer.hide(300)
        }

        loading = true
        submitButton.prop('disabled', true)
        closeButton.prop('disabled', true)
        submitButton.find('.spinner-border').show()
        closeButton.find('.spinner-border').show()

        const commissionData = {
            value: parseFloat(commissionValue),
            operation: commissionOperatorSelect.val(),
            use_percent: commissionUnitSelect.val() === 'percent'
        }

        const priceData = {
            value: parseFloat(priceValue),
            operation: priceOperatorSelect.val(),
            use_percent: priceUnitSelect.val() === 'percent'
        }

        try {
            await updateTariffs(
                tariffsList, 
                commissionValue ? commissionData : null,
                priceValue ? priceData : null
            )
            
            window.location.reload()
        } catch (error) {
            alert(error)
            loading = false
            submitButton.prop('disabled', false)
            closeButton.prop('disabled', false)
            submitButton.find('.spinner-border').hide()
            closeButton.find('.spinner-border').hide()
        }
    })
})