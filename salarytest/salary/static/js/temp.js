function checkAndSubmit() {
    const newSalary = parseInt(document.getElementById('salary').value);
    const oldSalary = parseInt(document.getElementById('oldSalary').value);
    const currentName = document.getElementById('name').value
    
    if (isNaN(newSalary)) {
        alert("변경할 급여를 입력하세요.");
        return;
    }

    if (newSalary < oldSalary) {
        if (!confirm("현재 금액보다 작은데 진행할까요?")) return;   
    }

    if (confirm(`${currentName}님 급여를 ${oldSalary} => ${newSalary} 로 변경합니다!!`)) {
        const form = document.getElementById('salaryForm');
        const id = document.createElement('input')
        id.value = {{ data.id }}
        id.id = 'id'
        id.name = 'id'
        
        form.appendChild(id)

        document.getElementById('salaryForm').submit();
    }
}