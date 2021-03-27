

const generatePopupNotification = function generatePopupNotification(message) {
  
  const colors = ["teal", "blue", "yellow", "red", "gray", "green"];
  const font_color = ["black", "white", "black", "white", "black", "black"];

  const random_color_index = Math.floor((Math.random() * 7) + 1);

  let notification = document.createElement("div");
  notification.className = "notification";
  notification.style.backgroundColor = colors[random_color_index];

  let notification_upper_bar = document.createElement("div");
  notification_upper_bar.className = "notification-upper-bar";
  notification_upper_bar.style.backgroundColor = colors[random_color_index];

  let notification_pin = document.createElement("img");
  notification_pin.className = "pin";
  notification_pin.src = "assets/pin.png";

  let notification_content = document.createElement("p");
  notification_content.className = "notification-content";
  notification_content.innerText = message;
  notification_content.style.color = font_color[random_color_index];
  
  notification_upper_bar.append(notification_pin);
  notification.append(notification_upper_bar);
  notification.append(notification_content);

  document.getElementById("popup").appendChild(notification);
  
}


messages_list = ["Lorem Ipsum", "Dolor emit", "This is motivating", "Welcome to MUACM", "Some facts are written here"];

function getNotification() {
  setTimeout(() => {
    let random_message_index = Math.floor((Math.random() * messages_list.length));
    generatePopupNotification(messages_list[random_message_index]);
    random_message_index = Math.floor((Math.random() * messages_list.length));
    generatePopupNotification(messages_list[random_message_index]);
  }, 600);
}

getNotification();