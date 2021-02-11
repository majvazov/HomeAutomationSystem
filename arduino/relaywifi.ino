#include <WiFi.h>

const char* wifi_name = "A1_A1C2CA"; // Your Wifi network name here
const char* wifi_pass = "72041880";    // Your Wifi network password here
WiFiServer server(80);    // Server will be at port 80

int relay_pin = 26;

void setup() 
{
  Serial.begin (115200);
  pinMode (relay_pin, OUTPUT);
  digitalWrite(relay_pin, HIGH);

  Serial.print ("Connecting to ");
  Serial.print (wifi_name);
  WiFi.begin (wifi_name, wifi_pass);     // Connecting to the wifi network

  while (WiFi.status() != WL_CONNECTED) // Waiting for the response of wifi network
  {
    delay (500);
    Serial.print (".");
  }
  Serial.println("");
  Serial.println("Connection Successful");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP()); 
  Serial.println("Type the above IP address into browser search bar"); 
  server.begin();
} 

void loop() 
{
  WiFiClient client = server.available();
  if (client)
  {
    boolean currentLineIsBlank = true;
    String buffer = "";  
    while (client.connected())
    {
      if (client.available())
      {
        char c = client.read(); 
        buffer+=c;
        if (c == '\n' && currentLineIsBlank)
        {
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println();    
          client.print("<HTML><title>ESP32</title>");
          client.print("<body><h1>ESP32 Standalone Relay Control </h1>");
          client.print("<p>Relay Control</p>");
          client.print("<a href=\"/?relayon\"\"><button>ON</button></a>");
          client.print("<a href=\"/?relayoff\"\"><button>OFF</button></a>");
          client.print("</body></HTML>");
          break;        // break out of the while loop:
        }
        if (c == '\n') { 
          currentLineIsBlank = true;
          buffer="";       
        } 
        else 
          if (c == '\r') {     
          if(buffer.indexOf("GET /?relayon")>=0)
            digitalWrite(relay_pin, HIGH);
          if(buffer.indexOf("GET /?relayoff")>=0)
            digitalWrite(relay_pin, LOW);   
        }
        else {
          currentLineIsBlank = false;
        }  
      }
    }
    client.stop();
  }
}
