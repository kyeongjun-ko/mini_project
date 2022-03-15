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
function doDisplay0(var1, novar1) {
    let t1 = var1;
    let f1 = novar1;

    for (let i = 0; i < t1.length; i++) {
        t = document.getElementById(t1[i]);
        t.style.display = 'block'
    }
    for (let i = 0; i < f1.length; i++) {
        f = document.getElementById(f1[i]);
        f.style.display = 'none';
    }
}

function doDisplay13(var1, novar1, novar2, novar3) {
    let t1 = document.getElementById(var1);
    let f1 = document.getElementById(novar1);
    let f2 = document.getElementById(novar2);
    let f3 = document.getElementById(novar3);

    t1.style.display = 'block';
    f1.style.display = 'none';
    f2.style.display = 'none';
    f3.style.display = 'none';
}

function getvalue(select){
    var idd = select[select.selectedIndex].value;
    var id = select[select.selectedIndex];
    console.log(id)
    return idd;
}