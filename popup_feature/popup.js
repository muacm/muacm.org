

const generatePopupNotification = function generatePopupNotification(message="close") {
  
  const colors = ["teal", "black", "blue", "purple", "red", "gray", "green"];
  const font_color = ["black", "white", "white", "white", "white", "black", "black"];

  const random_color_index = Math.floor((Math.random() * 7) + 1);

  let notification = document.createElement("div");
  notification.id = "stickynote";
  notification.style.backgroundColor = colors[random_color_index];

  let notification_content = document.createElement("p");
  notification_content.className = "quote";
  notification_content.innerText = message;
  notification.style.color = font_color[random_color_index];

  let notification_pin = document.createElement("img");
  notification_pin.src = "assets/pin.png";
  notification.className = "pin";

  if (message === "close") {
    document.getElementById("popup").lastChild.remove();
    console.log("closed notification...");
  } else {

    notification.append(notification_content);
    notification.append(notification_pin);
  
    document.getElementById("popup").appendChild(notification);
  }
}

messages_list = ["Lorem Ipsum", "Dolor emit", "This is motivating", "Welcome to MUACM", "Some facts are written here"];

function getNotification() {
  setTimeout(() => {
    let random_message_index = Math.floor((Math.random() * messages_list.length));
    generatePopupNotification(messages_list[random_message_index]);
  }, 600);
}

getNotification();