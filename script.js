$(document).ready(function() {
    $('#submit').click(function() {
        event.preventDefault(); // prevent PageReLoad
        // Validation
        
//      let length_key = Math.floor(Math.random() * 15);
//      var chars = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ";
//      var secretkey_length = length_key;
//      var secretkey = "";
//      
//      for (var i = 0; i <= passwordLength; i++) {
//          var randomNumber = Math.floor(Math.random() * chars.length);
//          password += chars.substring(randomNumber, randomNumber +1);
//      }
        
        var vid_decoded = $('#vid').val();
        
        var vid_encoded = btoa(vid_decoded);
        
        toString(vid_encoded)
        
        vid_encoded = vid_encoded.substr(4)
        
//      var validvid1 = $('#vid').val() === '691 374'; 
//      var validvid2 = $('#vid').val() === '187 637'; 
//      var validvid3 = $('#vid').val() === '691 375'; 
//      var validvid524113= $('#vid').val() === '524 113';
        console.log(vid_encoded);
        
        if (vid_encoded == "IDM3NA==") {
            window.location.replace("691374.html")
        }
        else if (vid_encoded == "IDYzNw==") {
            window.location.replace("187637.html")
        }
        else if (vid_encoded == "IDM3NQ==") {
            window.location.replace("691375.html")
        }
        else if (vid_encoded == "IDExMw==") {
            window.location.replace("524113.html")
        }
        else {
            window.location.replace("idnotfound.html")}
        
//      if (validvid1 == true) { // if ValidEmail & ValidPassword
//          $('#valid').css('display', 'block');
//          window.location.replace("691374.html");
//      }
//      else if (validvid2 == true) {
//          $('#valid').css('display', 'block');
//          window.location.replace("187637.html");
//      }
//      else if (validvid3 == true) {
//          $('#valid').css('display', 'block');
//          window.location.replace("691375.html");
//      }
//      else if (validvid524113 == true) {
//          $('#valid').css('display', 'block');
//          window.location.replace('524113.html');
//      }
//      else {
//          $('#error').css('display', 'block'); // show error msg
//          window.location.replace("idnotfound.html");
//      }
    });
});