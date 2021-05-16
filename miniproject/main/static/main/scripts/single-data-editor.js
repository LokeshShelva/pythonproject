
class SingleDataEditor extends HTMLElement {
    constructor() {
        super();
        this.createEditor();
    }

    createEditor() {
        this.tableWrapper = document.createElement("div");
        this.table = document.createElement("table");

        this.table.classList.add("no-padding");
        this.table.classList.add("no-hiding");

        this.tableWrapper.classList.add("table-wrapper");

        this.tableWrapper.append(this.table);
        this.append(this.tableWrapper);

        let addRowBtn = document.createElement("div");
        addRowBtn.classList.add("add-row-btn");
        addRowBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>ic_add_24px</title>
            <g>
                <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path>
            </g>
        </svg>
        New Row
        ` ;
        addRowBtn.addEventListener("click", () => this.addRow());

        this.header = this.table.createTHead();
        let headerRow = this.header.insertRow();
        headerRow.insertCell(-1).innerHTML = "#";
        headerRow.insertCell(-1).innerHTML = "Label";
        headerRow.insertCell(-1).innerHTML = "Value";
        headerRow.insertCell(-1);

        this.footer = this.table.createTFoot();
        let footerRow = this.footer.insertRow();
        footerRow.insertCell(-1);
        footerRow.insertCell(-1).append(addRowBtn);
        footerRow.insertCell(-1);
        footerRow.insertCell(-1);

        this.header = this.table.createTBody();
    }

    addRow() {
        let newRow = this.table.tBodies[0].insertRow(-1);
        let headerCells = [...this.table.tHead.rows[0].cells];
        headerCells.forEach((cell, i) => {
            let newCell = newRow.insertCell(-1);
            if (i == 1) {
                newCell.innerHTML = `
                <div class="entry-row">
                    <div data-name="label" contenteditable></div>
                    <div data-name="color"><input type="color"></div>
                </div>
                `;
            } else if (i > 1 && i != headerCells.length - 1) {
                let valueDiv = document.createElement("div");
                valueDiv.setAttribute("data-name", "value");
                valueDiv.contentEditable = true;
                valueDiv.addEventListener("keypress", e => {
                    var key = e.key;
                    if (!key.match(/[0-9.]/))
                        e.preventDefault();
                    if (key == "." && e.target.innerText.includes(".")) {
                        e.preventDefault();
                    }
                })
                newCell.append(valueDiv);
            } else if (i == headerCells.length - 1) {
                let deleteRowBtn = document.createElement("div");
                deleteRowBtn.classList.add("delete-row-btn");
                deleteRowBtn.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>ic_close_24px</title>
                    <g>
                        <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
                    </g>
                </svg>` ;
                deleteRowBtn.addEventListener("click", () => this.deleteRow(newRow));
                newCell.append(deleteRowBtn);
            }

        });
        this.updateSerialNumber();
        return newRow;
    }

    deleteRow(row) {
        row.remove();
        this.updateSerialNumber();
    }

    updateSerialNumber() {
        [...this.table.tBodies[0].rows].forEach((row, i) => {
            row.cells[0].innerText = i + 1;
        })
    }

    getData() {
        let dataSet = [];

        [...this.table.tBodies[0].rows].forEach((row) => {
            dataSet.push({
                name: row.querySelector(`[data-name="label"]`).innerText,
                color: row.querySelector(`[data-name="color"] input[type="color"]`).value,
                value: row.querySelector(`[data-name="value"]`).innerText,
                field: ""
            });
        });

        return dataSet;
    }

    parseArray(str = "") {
        str = str.replaceAll("[", "");
        str = str.replaceAll("]", "");
        str = str.replaceAll(" ", "");
        str = str.replaceAll("'", "");
        return str.split(",");
    }

    setData(dataSet) {
        dataSet.forEach((data) => {
            let color = data.color;
            let label = data.name;
            let value = data.value;

            let row = this.addRow();
            row.querySelector(`[data-name="label"]`).innerText = label;
            row.querySelector(`[data-name="color"] input[type="color"]`).value = color;
            row.querySelector(`[data-name="value"]`).innerText = value;

        })
    }

}

customElements.define("single-data-editor", SingleDataEditor);
