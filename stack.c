#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node *head;

void create(int n)
{
    struct node *ptr = (struct node *)malloc(sizeof(struct node));

    if (ptr == NULL)
    {
        printf("\nMemory not allocated!");
        return;
    }

    ptr->data = n;
    ptr->next = NULL;
    head = ptr;
    printf("\nNew Stack created!");
}

void insert(int n)
{
    if (head == NULL)
    {
        printf("\nNO stack!");
        return;
    }
    struct node *ptr = (struct node *)malloc(sizeof(struct node));
    ptr->data = n;
    ptr->next = head;
    head = ptr;
    printf("\n%d inserted!");
}

void delete()
{
    if (head == NULL)
    {
        printf("\nStack is underflow!");
        return;
    }

    struct node *ptr = head;
    head = head->next;

    printf("\n%d is deleted!", ptr->data);
    free(ptr);
}

void display()
{
    if (head == NULL)
    {
        printf("\nUnderflow");
        return;
    }
    struct node *ptr = head;
    printf("\nData of stack: ");
    while (ptr != NULL)
    {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
}

int main()
{
    while (1)
    {
        int choice;
        printf("\n\t\t <--Stack--> \n Menu :\n1. Create\n2. insert\n3. Delete\n4. Display\n5. Exit\n");
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