function showOKFlash() {
  const flash = document.getElementById("flash_ok");
  flash.classList.add("active");

  setTimeout(() => {
    const flash = document.getElementById("flash_ok");
    flash.classList.remove("active");
  }, 3000);
}

function showErrorFlash() {
  const flash = document.getElementById("flash_err");
  flash.classList.add("active");

  setTimeout(() => {
    const flash = document.getElementById("flash_err");
    flash.classList.remove("active");
  }, 3000);
}
