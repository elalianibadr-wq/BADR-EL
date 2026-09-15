export class Student {
    constructor(nom, age, note) {
        this.nom = nom;
        this.age = age;
        this.note = note;
    }

    afficherInfo() {
        console.log(`Nom : ${this.nom}`);
        console.log(`Age : ${this.age}`);
        console.log(`Note : ${this.note}`);
    }

    estAdmis() {
        return this.note >= 10;
    }
}
