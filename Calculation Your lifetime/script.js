
function alerts(){
    console.clear()
}

function calculation(){
    var ad = document.getElementById('a1').value;
    var soyad = document.getElementById('a2').value;
    var dogumgunu = document.getElementById('a3').value;
    var birthday = new Date(dogumgunu)
    var now = new Date();

    var millisaniya = now - birthday;
    var saniye = millisaniya/1000;
    var deqiqe = saniye/60;
    var saat = deqiqe/60;
    var gun = saat/24;
    var ay = gun/30;
    var il = ay/12-1;

    console.log(ad,soyad);
    console.log('Doğum gününüz:',birthday);
    console.log('Hal hazirki tarix:',now);
    console.log();

    console.log('Hörmətli', ad, soyad, 'sizin indiyə qədər bu dünyada keçirdiyiniz müddət:');
    console.log('İl:', il);
    console.log("Ay:", ay);
    console.log("Gün:", gun);
    console.log("Saat:", saat);
    console.log("Dəqiqə:", deqiqe);
    console.log("Saniyə:", saniye);
    console.log("Mm:",millisaniya);
}
