function doDisplay(vars) {
    let ddd = document.getElementById(vars);
    // let nnn = document.getElementById(novars);
    ddd.style.display = 'block';
    // nnn.style.display = 'none'
}

function doClose(vars) {
    let ddd = document.getElementById(vars);
    ddd.style.display = 'none';
}
// ============================
function doDisplay3(vars, novar1, novar2) {
    let t = document.getElementById(vars);
    let f1 = document.getElementById(novar1);
    let f2 = document.getElementById(novar2);
    t.style.display = 'block';
    f1.style.display = 'none'
    f2.style.display = 'none'
}