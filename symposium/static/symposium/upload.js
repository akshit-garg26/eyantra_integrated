document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll(".inp").forEach(input => {
        input.addEventListener('input', () => {
            let allFilled = true;
            Array.from(document.querySelectorAll(".inp")).forEach(field => {
              if (!field.value) {
                allFilled = false;
              }
            });
            document.querySelector('input[type="submit"]').disabled = !allFilled;
        });
    });

  document.getElementById("input-value1").addEventListener("change", (e)=>{document.getElementById("span1").innerText = e.target.value});
  document.getElementById("input-value2").addEventListener("change", (e)=>{document.getElementById("span2").innerText = e.target.value});
  document.getElementById("input-value3").addEventListener("change", (e)=>{document.getElementById("span3").innerText = e.target.value});
})