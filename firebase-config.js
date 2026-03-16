// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getFirestore} from "firebase/firestore";
const firebaseConfig = {
  apiKey: "AIzaSyCfoMo2I0wjFEtNbUuHQ2sHW2M_bnqB8rc",
  authDomain: "marie-vinodh-wedding.firebaseapp.com",
  projectId: "marie-vinodh-wedding",
  storageBucket: "marie-vinodh-wedding.firebasestorage.app",
  messagingSenderId: "1072481959116",
  appId: "1:1072481959116:web:a495735d3ed87b66d41669",
  measurementId: "G-KMVCSV4PHT"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const db = getFirestore(app);