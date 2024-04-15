document.addEventListener('DOMContentLoaded', function () {
          const flashErr = document.getElementById('flash_ok');

          flashErr.addEventListener('animationend', function () {
            flashErr.remove();
          });
        });

document.addEventListener('DOMContentLoaded', function () {
        const flashErr = document.getElementById('flash_err');

        flashErr.addEventListener('animationend', function () {
          flashErr.remove();
        });
      });
