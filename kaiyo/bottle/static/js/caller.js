
var SERVER_URL = "http://172.20.10.2:8080/"




setInterval(getButton, 200)
// -----------------------------------------------------------------------------------------
var alpha = 0, beta = 0, gamma = 0;             // ジャイロの値を入れる変数を3個用意

// ジャイロセンサの値が変化したら実行される deviceorientation イベント
window.addEventListener("deviceorientation", (dat) => {
    alpha = dat.alpha;  // z軸（表裏）まわりの回転の角度（反時計回りがプラス）
    beta  = dat.beta;   // x軸（左右）まわりの回転の角度（引き起こすとプラス）
    gamma = dat.gamma;  // y軸（上下）まわりの回転の角度（右に傾けるとプラス）

    alpha = Math.round(alpha * 10) / 10
    beta  = Math.round(beta * 10) / 10
    gamma = Math.round(gamma * 10) / 10
});

// 指定時間ごとに繰り返し実行される setInterval(実行する内容, 間隔[ms]) タイマーを設定
// var timer = window.setInterval(() => {
//     displayData();      // displayData 関数を実行
//     // setLed(999, 999);
// }, 333); // 33msごとに（1秒間に約30回）

var timer2 = window.setInterval(() => {
    setLed(0, -1);
    displayData();
}, 50); // 33msごとに（1秒間に約30回）


// データを表示する displayData 関数
function displayData() {
    var txt = document.getElementById("txt");   // データを表示するdiv要素の取得
    txt.innerHTML = "yaw : "    + alpha + "<br>"  // x軸の値
                  + "pitch : "  + beta  + "<br>"  // y軸の値
                  + "roll : "   + gamma;          // z軸の値
}

// -----------------------------------------------------------------------------------------
var slider_old1 = 0
var slider_old2 = 0
var slider_old3 = 0

function setLed(number, slider) {
  if(slider == -1);
  else{
    if(number == 1) slider_old1 = slider;
    if(number == 2) slider_old2 = slider;
    if(number == 3) slider_old3 = slider;
  }


  callApi(
      SERVER_URL + "setLed",
      {
          // "num": displayData(),
          "yaw": alpha,
          "pitch": beta,
          "roll": gamma,
          "slider1": slider_old1,
          "slider2": slider_old2,
          "slider3": slider_old3
      },
      function (o) {
      });
}


function getButton() {
    callApi(
        SERVER_URL + "getButton",
        {"dummy":"dummy"},
        function (o) {
            console.log(o.responseText);
            var retJson = eval('new Object(' + o.responseText + ')');
            document.getElementById("checkbox-button-0").checked = retJson.btn_0 == "1";
            document.getElementById("checkbox-button-1").checked = retJson.btn_1 == "1";
        });
}

function callApi(url, jsonObj, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('Accept', 'application/json');

    xhr.onreadystatechange = (function(myxhr) {
        return function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                callback(myxhr);
            }
        }
    })(xhr);

    xhr.send(JSON.stringify(jsonObj));
}
