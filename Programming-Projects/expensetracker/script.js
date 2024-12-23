const descriptionInput = document.getElementById('description');
const amountInput = document.getElementById('amount');
const categorySelect = document.getElementById('category');
const typeSelect = document.getElementById('type');
const addButton = document.getElementById('add');
const transactionList = document.getElementById('transaction-list');
const balanceDisplay = document.getElementById('balance');

let transactions = [];
let balance = 0;

function updateUI() {

    balanceDisplay.textContent = balance.toFixed(2);
    transactionList.innerHTML = '';

    transactions.forEach((transaction, index) => {
        const transactionItem = document.createElement('li');
        transactionItem.innerHTML = `
            <span>${transaction.description} - $${transaction.amount.toFixed(2)} (${transaction.category})</span>
            <button class="delete-btn" onclick="deleteTransaction(${index})">Delete</button>
        `;
        transactionList.appendChild(transactionItem);
    });
}
function addTransaction() {
    const description = descriptionInput.value.trim();
    const amount = parseFloat(amountInput.value);
    const category = categorySelect.value;
    const type = typeSelect.value;

    if (description && !isNaN(amount) && amount > 0) {
        const transaction = { description, amount, category, type };
        if (type === 'Expense') {
            balance -= amount;
        } else {
            balance += amount;
        }
        descriptionInput.value = '';
        amountInput.value = '';
        updateUI();
    } else {
        alert('Please provide valid description and amount.');
    }
}
function deleteTransaction(index) {
    const transaction = transactions[index];

    if (transaction.type === 'Expense') {
        balance += transaction.amount;
    } else {
        balance -= transaction.amount;
    }
    transactions.splice(index, 1);
    updateUI();
}
addButton.addEventListener('click', addTransaction);
updateUI();
