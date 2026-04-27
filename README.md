# expense-tracker-django
A simple expense tracker web app built with Django


# 🗂️ Expense Tracker — Scrum Sprints

## Product Backlog

**User Stories:**
- As a user, I want to see all my expenses
- As a user, I want to add a new expense
- As a user, I want to edit an expense
- As a user, I want to delete an expense
- As a user, I want to see the total of my expenses
- As a user, I want to filter expenses by category

---

## 🏃 Sprint 1 — Project Setup
**Duration:** 1-2 days

**Tasks:**
- [ ] Mag-setup ng Django project
- [ ] Mag-setup ng Django app (`expenses`)
- [ ] Gumawa ng `Expense` model
- [ ] Mag-run ng migrations
- [ ] Mag-register ng model sa admin
- [ ] Mag-setup ng base template (`base.html`)

**Acceptance Criteria:**
- [ ] Tumatakbo ang Django server nang walang error
- [ ] Makikita ang `Expense` model sa Django admin
- [ ] Naka-apply ang migrations sa database
- [ ] May `base.html` na template na nagse-serve

---

## 🏃 Sprint 2 — READ
**Duration:** 1 day

**Tasks:**
- [ ] Gumawa ng `expense_list` view
- [ ] Gumawa ng URL para sa list
- [ ] Gumawa ng `expense_list.html` template 
- [ ] I-display ang lahat ng expenses sa table
- [ ] I-display ang total ng lahat ng expenses

**Acceptance Criteria:**
- [ ] Pumupunta sa list page ang user sa `/`
- [ ] Nakikita ang lahat ng expenses sa table
- [ ] Nakikita ang total amount sa ibaba ng table
- [ ] Kung walang expenses, may mensahe na "No expenses yet"

---

## 🏃 Sprint 3 — CREATE
**Duration:** 1 day

**Tasks:**
- [ ] Gumawa ng `expense_create` view
- [ ] Gumawa ng URL para sa create
- [ ] Gumawa ng `expense_create.html` template
- [ ] Mag-add ng form para sa bagong expense
- [ ] Mag-redirect sa list after save

**Acceptance Criteria:**
- [ ] Pumupunta sa create page ang user sa `/create/`
- [ ] May form na may fields: title, amount, category, date, notes
- [ ] Kapag nag-submit → nase-save sa database
- [ ] Kapag nase-save → nire-redirect sa list page
- [ ] Nakikita ang bagong expense sa list

---

## 🏃 Sprint 4 — UPDATE
**Duration:** 1 day

**Tasks:**
- [ ] Gumawa ng `expense_update` view
- [ ] Gumawa ng URL para sa update
- [ ] Gumawa ng `expense_update.html` template
- [ ] Pre-fill ang form ng existing data
- [ ] Mag-redirect sa list after save

**Acceptance Criteria:**
- [ ] Pumupunta sa update page ang user sa `/update/<pk>/`
- [ ] Pre-filled ang form ng existing data ng expense
- [ ] Kapag nag-edit → nase-save ang changes sa database
- [ ] Kapag nase-save → nire-redirect sa list page
- [ ] Nakikita ang updated na expense sa list
- [ ] Kapag invalid ang pk → 404 page ang lalabas

---

## 🏃 Sprint 5 — DELETE
**Duration:** 1 day

**Tasks:**
- [ ] Gumawa ng `expense_delete` view
- [ ] Gumawa ng URL para sa delete
- [ ] Gumawa ng `expense_delete.html` template
- [ ] Mag-add ng confirmation page bago mag-delete
- [ ] Mag-redirect sa list after delete

**Acceptance Criteria:**
- [ ] Pumupunta sa delete page ang user sa `/delete/<pk>/`
- [ ] Nakikita ang confirmation message na may pangalan ng expense
- [ ] Kapag nag-click ng **Yes, Delete** → nababura sa database
- [ ] Kapag nababura → nire-redirect sa list page
- [ ] Kapag nag-click ng **Cancel** → bumabalik sa list, walang nangyari
- [ ] Kapag invalid ang pk → 404 page ang lalabas

---

## 🏃 Sprint 6 — Extra Features
**Duration:** 1-2 days

**Tasks:**
- [ ] Mag-add ng filter by category sa list page
- [ ] Mag-add ng total per category
- [ ] Mag-improve ng UI (pwede Bootstrap)

**Acceptance Criteria:**
- [ ] May dropdown filter ng category sa list page
- [ ] Kapag nag-filter → nagpapakita lang ng expenses ng selected category
- [ ] Nakikita ang total per category
- [ ] Maayos ang UI — readable at presentable

---

## 🏃 Sprint 7 — Final Polish
**Duration:** 1 day

**Tasks:**
- [ ] Mag-test ng lahat ng features
- [ ] Mag-fix ng bugs
- [ ] Mag-add ng README sa project
- [ ] I-push sa GitHub

**Acceptance Criteria:**
- [ ] Lahat ng CRUD features ay gumagana nang walang error
- [ ] May README na naglalaman ng: project description, setup instructions, features
- [ ] Naka-push sa GitHub ang project
- [ ] Walang debug errors na nakikita sa browser

---

## 📊 Summary

| Sprint | Focus | Duration |
|--------|-------|----------|
| 1 | Setup | 1-2 days |
| 2 | Read | 1 day |
| 3 | Create | 1 day |
| 4 | Update | 1 day |
| 5 | Delete | 1 day |
| 6 | Extra Features | 1-2 days |
| 7 | Final Polish | 1 day |
| **Total** | | **7-9 days** |