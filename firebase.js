// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAkNIG_YRdwXEZ4n-0WNrTUsUZzSJ7M12s",
  authDomain: "rental-manager-aee74.firebaseapp.com",
  projectId: "rental-manager-aee74",
  storageBucket: "rental-manager-aee74.appspot.com",
  messagingSenderId: "119665802639",
  appId: "1:119665802639:web:64c702a55bec54a0e71ffa",
  measurementId: "G-MEMCK0WLYF"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);