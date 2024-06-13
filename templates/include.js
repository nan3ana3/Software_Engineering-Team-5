// include.js
document.addEventListener("DOMContentLoaded", function () {
    const includeElements = document.querySelectorAll('[data-include]');
    includeElements.forEach((element) => {
        const file = element.getAttribute('data-include');
        fetch(file)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.text();
            })
            .then(data => {
                element.innerHTML = data;

                // CSS 파일 로드
                const link = document.createElement('link');
                link.rel = 'stylesheet';
                link.href = '../static/css/navigation.css'; // CSS 파일 경로
                document.head.appendChild(link);

                // 네비게이션 버튼 이벤트 추가
                const buttonMain = document.getElementById("buttonMain");
                if (buttonMain) {
                    buttonMain.addEventListener("click", function (e) {
                        window.location.href = "./index.html";
                    });
                }

                const buttonDM = document.getElementById("buttonDM");
                if (buttonDM) {
                    buttonDM.addEventListener("click", function (e) {
                        window.location.href = "./recieved-d-m.html";
                    });
                }

                const buttonMypage = document.getElementById("buttonMypage");
                if (buttonMypage) {
                    buttonMypage.addEventListener("click", function (e) {
                        window.location.href = "./my-page.html";
                    });
                }

                const buttonLogout = document.getElementById("buttonLogout");
                if (buttonLogout) {
                    buttonLogout.addEventListener("click", function (e) {
                        window.location.href = "./index.html";
                    });
                }
            })
            .catch(error => {
                console.error('Error loading the include file:', error);
            });
    });
});
