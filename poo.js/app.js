import { Student } from "./Student.js";

const student1 = new Student("Salah", 15, 14);
const student2 = new Student("Amin", 25, 8);

student1.afficherInfo();
console.log("Admis :", student1.estAdmis());

console.log("----------------");

student2.afficherInfo();
console.log("Admis :", student2.estAdmis());
