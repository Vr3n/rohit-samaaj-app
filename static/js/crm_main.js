document.addEventListener("DOMContentLoaded", function () {
  const logout_btn = document.getElementById("logout_button");

  logout_btn.addEventListener('click', () => {
    Swal.fire({ 
      title: 'Are you sure?',
      text: 'You want to logout!',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Logout',
      cancelButtonColor: '#d33',
      confirmButtonColor: '#3085d6',
      heightAuto: false
    }).then((result) => {
      if (result.isConfirmed) {
        htmx.trigger("#logout_button", "confirmed");
      } else {
        const Toast = Swal.mixin({
          toast: true,
          position: 'top-end',
          showConfirmButton: false,
          timer: 3000,
          timerProgressBar: true,
          didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
          }
        })
        
        Toast.fire({
          icon: 'success',
          title: "Ok, I'm not signing you out. ✌"
        })
      }
    })
  })
});
