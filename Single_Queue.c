#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node *front;
struct node *rear;

void create(int n){
    struct node *ptr = (struct node*)malloc(sizeof(struct node));
    ptr->data = n;
    ptr->next = NULL;
    front = rear = ptr;
    printf("\nNew Queue is created!");
}

void insert(int n){
    if(rear == NULL){
        printf("\nCreate queue first!");
        return;
    }
    struct node *ptr = (struct node*)malloc(sizeof(struct node));
    ptr->data = n;
    ptr->next = NULL;
    rear->next = ptr;
    rear = ptr;
    printf("\n%d is inserted!",rear->data);
}

void delete(){
    if(front == NULL){
        printf("\nUnderFlow!");
        return;
    }
    struct node *ptr = front;
    if(front == rear)
        rear = NULL;
    front = front->next;
    printf("\n%d is deleted!",ptr->data);
    free(ptr);
}

void display(){
    if(front==NULL){
        printf("\nUnderFlow Queue!");
        return;
    }
    struct node *ptr = front;

    printf("\nQueue data:");
    while(ptr != NULL){
        printf(" %d",ptr->data);
        ptr = ptr->next;
    }
}

int main()
{
    while (1)
    {
        int choice;
        printf("\n\t\t <--Single Queue--> \n Menu :\n1. Create\n2. Insert\n3. Delete\n4. Display\n5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
        {
            int n;
            printf("\nEnter the data: ");
            scanf("%d", &n);
            create(n);
            break;
        }
        case 2:
        {
            int n;
            printf("\nEnter the data: ");
            scanf("%d", &n);
            insert(n);
            break;
        }
        case 3:
        {
            delete();
            break;
        }
        case 4:
        {
            display();
            break;
        }
        case 5:
        {
            return 0;
        }
        default:
            printf("\nInvalid Choice!");
        }
    }
}